from pydantic import BaseModel
from typing import Optional, Dict

class LoreRequest(BaseModel):
    content: str
    metadata: Optional[Dict] = {}