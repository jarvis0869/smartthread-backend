from app.api.threads import router as api_router
from pydantic import BaseModel
from typing import List
from datetime import datetime

router = APIRouter(prefix="/threads", tags=["Threads"])

class Thread(BaseModel):
    id: str
    title: str
    summary: str
    source: str
    status: str
    createdAt: datetime
    messageCount: int

@router.get("/", response_model=List[Thread])
def get_threads():
    return [
        {
            "id": "abc123",
            "title": "Finalize login flow",
            "summary": "Team discussed changes to login process",
            "source": "slack",
            "status": "processed",
            "createdAt": datetime.now(),
            "messageCount": 6
        }
    ]
