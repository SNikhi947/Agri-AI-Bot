from typing import Optional
from sqlmodel import Field, SQLModel
from datetime import datetime

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    region: Optional[str] = "India"
    language: str = "en"

class ChatMessage(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int
    role: str  # "user" or "bot"
    text: str
    timestamp: datetime = Field(default_factory=datetime.now)
    meta_json: Optional[str] = "{}" # Stores structured data like detected pest info

# Pydantic Models for API Communication
class ChatRequest(SQLModel):
    user_id: int
    message: str
    language: str = "en"