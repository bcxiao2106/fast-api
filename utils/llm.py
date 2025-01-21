from langchain_community.llms import Ollama
from config.settings import settings
import aiohttp
import json
from typing import Optional
from langchain.schema.language_model import BaseLanguageModel
import logging

logger = logging.getLogger(__name__)

async def validate_ollama_model(model: str) -> bool:
    """
    Validate that the model exists in Ollama.
    
    Args:
        model (str): The model name to validate
        
    Returns:
        bool: True if model exists, False otherwise
    """
    try:
        timeout = aiohttp.ClientTimeout(total=30)  # 30 second timeout
        async with aiohttp.ClientSession(timeout=timeout) as session:
            logger.info(f"Checking for model: {model}")
            async with session.get(f"{settings.OLLAMA_BASE_URL}/api/tags") as response:
                if response.status != 200:
                    logger.error(f"Failed to get models list. Status: {response.status}")
                    return False
                data = await response.json()
                # Strip :latest suffix for comparison if present
                model_name = model[:-7] if model.endswith(':latest') else model
                available_models = [
                    m["name"][:-7] if m["name"].endswith(':latest') else m["name"]
                    for m in data.get("models", [])
                ]
                logger.info(f"Available models: {available_models}")
                logger.info(f"Looking for model: {model_name}")
                return model_name in available_models
    except Exception as e:
        logger.error(f"Error validating model: {str(e)}", exc_info=True)
        return False

def get_llm(model_name: Optional[str] = None) -> BaseLanguageModel:
    """
    Initialize and return an Ollama LLM instance.
    
    Args:
        model_name (str, optional): The name of the Ollama model to use. 
            Defaults to the one specified in settings.
    
    Returns:
        Ollama: An instance of the Ollama LLM
    """
    model = model_name or settings.OLLAMA_MODEL
    if not model.endswith(':latest'):
        model = f"{model}:latest"
        
    return Ollama(
        base_url=settings.OLLAMA_BASE_URL,
        model=model,
        temperature=0.7,  # Add some temperature for more creative responses
        timeout=120.0,  # Increase timeout to 2 minutes
    )
