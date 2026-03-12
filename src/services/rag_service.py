from src.services.embedding_service import embed_text
from src.services.chroma_service import search_lore
from src.services.ollama_service import generate_text
from src.utils.prompt_builder import build_prompt


def generate_story(user_prompt, temperature, top_p):

    # Step 1 — Convert prompt to embedding
    embedding = embed_text(user_prompt)

    # Step 2 — Retrieve relevant lore from ChromaDB
    context_docs = search_lore(embedding)

    # Step 3 — Build final prompt with lore context
    final_prompt = build_prompt(user_prompt, context_docs)

    # Step 4 — Send to Ollama LLM
    return generate_text(final_prompt, temperature, top_p)