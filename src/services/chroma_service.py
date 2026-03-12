import chromadb
import uuid
from src.config import CHROMA_COLLECTION

# Initialize ChromaDB client
client = chromadb.Client()

# Create or load collection
collection = client.get_or_create_collection(
    name=CHROMA_COLLECTION
)


def add_lore(text, embedding, metadata):
    """
    Store lore entry in vector database
    """

    doc_id = str(uuid.uuid4())

    collection.add(
        documents=[text],
        embeddings=[embedding],
        ids=[doc_id],
        metadatas=[metadata]
    )

    return doc_id


def search_lore(embedding, k=3):
    """
    Retrieve top-k similar lore entries
    """

    results = collection.query(
        query_embeddings=[embedding],
        n_results=k
    )

    return results["documents"][0]