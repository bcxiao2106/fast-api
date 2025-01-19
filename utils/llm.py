from langchain_community.llms import Ollama
from config.settings import settings

def get_ollama_llm(model_name: str = None):
    """
    Initialize and return an Ollama LLM instance.
    
    Args:
        model_name (str, optional): The name of the Ollama model to use. 
            Defaults to the one specified in settings.
    
    Returns:
        Ollama: An instance of the Ollama LLM
    """
    return Ollama(
        base_url=settings.OLLAMA_BASE_URL,
        model=model_name or settings.OLLAMA_MODEL,
    )
