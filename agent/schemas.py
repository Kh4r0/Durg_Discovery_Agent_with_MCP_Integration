# agent/schemas.py
from pydantic import BaseModel
from typing import List, Dict

class AgentResponse(BaseModel):
    answer: str
    fact_check: Dict
    recommendations: Dict
