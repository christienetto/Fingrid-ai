from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import logging

from ai import PostAnalysisSystem

chatbot = PostAnalysisSystem()

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatMessage(BaseModel):
    message: str

@app.post("/api/chat")
async def chat(message: ChatMessage):
    try:
        logger.info(f"Received message: {message.message}")
        response = chatbot.chat_with_ai(message.message)
        # analyse post has the current info: response["summary"] and response["categories"]
        logger.info(f"Sending response: {response}")
        return {"response": response}
    except Exception as e:
        logger.error(f"Error processing message: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

# Basic health check endpoint
@app.get("/api/health")
async def health_check():
    return {"status": "ok"}