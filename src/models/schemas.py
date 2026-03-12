from pydantic import BaseModel
from typing import Optional, Dict


class LoreRequest(BaseModel):
    content: str
    metadata: Optional[Dict] = {}


class GenerationParameters(BaseModel):
    temperature: Optional[float] = 0.7
    top_p: Optional[float] = 0.9


class GenerateRequest(BaseModel):
    prompt: str
    parameters: Optional[GenerationParameters]