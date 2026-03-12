from sentence_transformers import SentenceTransformer
from src.config import EMBEDDING_MODEL_NAME

model = SentenceTransformer(EMBEDDING_MODEL_NAME)

def embed_text(text: str):
    embedding = model.encode(text)
    return embedding.tolist()