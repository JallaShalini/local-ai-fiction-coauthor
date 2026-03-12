from pathlib import Path

# Load persona instructions
persona = Path("prompts/persona.md").read_text()

def build_prompt(user_prompt, context_docs):

    # Combine retrieved lore documents
    context = "\n".join(context_docs)

    # Build final prompt for LLM
    return f"""
{persona}

Context from lorebook:
{context}

Continue the story:

{user_prompt}
"""