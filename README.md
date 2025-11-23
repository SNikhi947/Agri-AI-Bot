# 🌾 Agri-AI-Bot: An Expert Indian Agriculture Consultant Chatbot

## ✨ Overview
This is a Full-Stack Web Application designed to provide instant, practical advice to Indian farmers on topics like crop management, pest control, and market price estimates.

The application uses a **Hybrid Logic** approach: fast, hardcoded responses for common queries (like weather or price) and intelligent responses from a powerful Large Language Model (LLM) for complex agricultural questions.

## 🛠️ Tech Stack & Architecture

| Component | Technology | Purpose |
| :--- | :--- | :--- |
| **Backend API** | **FastAPI** (Python) | High-performance, asynchronous REST API for handling requests. |
| **AI Model** | **Google Gemini 2.0 Flash** | Provides fast, accurate, and context-aware agricultural advice. |
| **Database** | **SQLModel / SQLite** | Simple ORM and database for persistent storage of all chat history. |
| **Frontend** | **HTML, CSS, JavaScript** | Simple, single-page interface to interact with the FastAPI backend. |
| **Dependencies** | `python-dotenv` | Securely manages the API key using environment variables. |

---
