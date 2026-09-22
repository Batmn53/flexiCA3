from pydantic import BaseModel
from typing import Literal

class MessageAnalysis(BaseModel):
    message: str
    importance: Literal["Important", "Normal"]
    category: Literal[
        "Academic",
        "Work",
        "Personal",
        "Financial",
        "Security",
        "General"
    ]
    priority: Literal["High", "Medium", "Low"]
    action: Literal[
        "Notify Immediately",
        "Review Later",
        "Ignore"
    ]
    reason: str
