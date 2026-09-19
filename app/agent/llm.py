from langchain_groq import ChatGroq

from app.config import LLM_MODEL


def get_llm():
    # Reads GROQ_API_KEY from the environment automatically
    return ChatGroq(model=LLM_MODEL, max_tokens=1000)
