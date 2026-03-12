from sentence_transformers import SentenceTransformer
from src.config import EMBEDDING_MODEL_NAME

# Load embedding model
model = SentenceTransformer(EMBEDDING_MODEL_NAME)


def embed_text(text: str):
    """
    Convert input text into vector embedding
    """

    embedding = model.encode(text)

    return embedding.tolist()