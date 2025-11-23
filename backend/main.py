from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from backend.db import create_db_and_tables
from backend.routers import pest_router, chat_router
import json
import os

app = FastAPI(title="AgriAI Assistant", version="1.0")

# CORS for Frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include Routers
app.include_router(pest_router.router)
app.include_router(chat_router.router)

# Load Translations
translations = {}
for lang in ["en", "hi", "te"]:
    try:
        with open(f"backend/translations/{lang}.json", encoding="utf-8") as f:
            translations[lang] = json.load(f)
    except:
        print(f"Warning: Could not load {lang}.json")

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

@app.get("/languages")
def get_translations():
    return translations

@app.get("/health")
def health_check():
    return {"status": "active", "system": "AgriAI v1.0"}

# Serve uploads just for demo viewing
app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("backend.main:app", host="0.0.0.0", port=8000, reload=True)