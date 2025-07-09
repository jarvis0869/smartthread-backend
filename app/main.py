from fastapi import FastAPI
from app.api import threads, processor

app = FastAPI()

app.include_router(threads.router)
app.include_router(processor.router)  # ← THIS is what enables /process-thread
