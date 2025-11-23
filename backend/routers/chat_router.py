# === FILE: backend/routers/chat_router.py ===
from fastapi import APIRouter, Depends
from sqlmodel import Session
from backend.db import get_session
from backend.models import ChatRequest, ChatMessage
import google.generativeai as genai
import os

router = APIRouter(tags=["chat"])

# ==========================================
# 🔑 CONFIGURE AI (GEMINI)
# ==========================================
# Your working key
API_KEY = "AIzaSyB2IZcFJWX8P8jiwJsaqvGfmZ-d_QxaZS4" 
genai.configure(api_key=API_KEY)

# ✅ CHANGED: Using a model from your "Allowed List"
model = genai.GenerativeModel('gemini-2.0-flash')

@router.post("/chat")
def chat_endpoint(request: ChatRequest, db: Session = Depends(get_session)):
    # 1. Save User Message
    user_msg = ChatMessage(user_id=request.user_id, role="user", text=request.message)
    db.add(user_msg)
    db.commit()
    
    # 2. Logic: Hybrid (Rules + AI)
    msg_lower = request.message.lower()
    bot_response_text = ""
    
    # SYSTEM INSTRUCTION: Tells the AI how to behave
    system_prompt = (
        "You are an expert Indian Agriculture Consultant. "
        "Answer in short, simple English sentences. "
        "Focus on practical farming advice, fertilizers, and pest control. "
        "If asked about prices, give average Indian market estimates in Rupees. "
        "Keep the tone helpful and encouraging."
    )

    try:
        # --- LAYER 1: Hardcoded Rules (Fast & Free) ---
        if "price" in msg_lower and "market" in msg_lower:
            bot_response_text = "Today's average prices: Tomato ₹25/kg, Onion ₹35/kg, Wheat ₹2200/quintal. Prices vary by mandi."
        elif "weather" in msg_lower and "forecast" in msg_lower:
            bot_response_text = "Forecast: Sunny, 32°C. Humidity 60%. No rain expected for the next 3 days."
        
        # --- LAYER 2: Real AI (Gemini 2.0) ---
        else:
            # We combine system prompt + user message
            full_prompt = f"{system_prompt}\n\nUser Question: {request.message}"
            response = model.generate_content(full_prompt)
            bot_response_text = response.text

    except Exception as e:
        # Fallback if API fails
        bot_response_text = "I am having trouble connecting to the satellite. Please check your internet connection."
        print(f"❌ AI ERROR: {e}")

    # 3. Save Bot Response
    bot_msg = ChatMessage(user_id=request.user_id, role="bot", text=bot_response_text)
    db.add(bot_msg)
    db.commit()
    
    return {"response": bot_response_text}