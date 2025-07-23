from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
from app.api.threads import router as api_router 
app.include_router(api_router, prefix="/api"
)
@app.get("/")
async def root():
    return {"message": "Hello World"}       
from pydantic import BaseModel

class Input(BaseModel):
    text: str

@app.post("/generate")
async def generate(input: Input):
    return {"response": f"Got: {input.text}"}

@app.get("/")
async def root():
    return {"message": "Hello World"}


