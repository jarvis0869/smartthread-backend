from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List
from app.ai.summarizer import generate_summary

router = APIRouter(prefix="/process-thread", tags=["Processor"])

class Message(BaseModel):
    author: str
    content: str
    timestamp: str

class ProcessRequest(BaseModel):
    thread: List[Message]

@router.post("/")
def process_thread(req: ProcessRequest):
    try:
        return generate_summary(req.thread)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
