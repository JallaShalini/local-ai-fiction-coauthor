from fastapi import APIRouter
from src.models.schemas import GenerateRequest
from src.services.rag_service import generate_story

router = APIRouter()

@router.post("/generate")
def generate_story_endpoint(request: GenerateRequest):

    result = generate_story(
        request.prompt,
        request.parameters.temperature if request.parameters else None,
        request.parameters.top_p if request.parameters else None
    )

    return {"story_segment": result}