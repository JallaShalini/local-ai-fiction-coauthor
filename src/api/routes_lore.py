from fastapi import APIRouter
from src.services.embedding_service import embed_text
from src.services.chroma_service import add_lore
from src.models.schemas import LoreRequest

router = APIRouter()

@router.post("/lore", status_code=201)
def add_lore_endpoint(request: LoreRequest):

    # Generate embedding for the lore text
    embedding = embed_text(request.content)

    # Store lore in ChromaDB
    doc_id = add_lore(request.content, embedding, request.metadata)

    return {
        "status": "success",
        "id": doc_id
    }