import uuid
import chromadb
from src.config import CHROMA_COLLECTION

client = chromadb.Client()

collection = client.get_or_create_collection(
    name=CHROMA_COLLECTION
)

def add_lore(text, embedding, metadata):

    doc_id = str(uuid.uuid4())

    collection.add(
        documents=[text],
        embeddings=[embedding],
        metadatas=[metadata],
        ids=[doc_id]
    )

    return doc_id