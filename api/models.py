from typing import List
from pydantic import BaseModel


class ReviewRequest(BaseModel):
    review: str


class SentimentResponse(BaseModel):
    label: str | None = None
    score: float | None = None


