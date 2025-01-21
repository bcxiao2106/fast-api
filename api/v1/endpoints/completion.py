from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from utils.llm import get_llm, validate_ollama_model
from chains.completion import CompletionChain
import logging
from langchain_community.llms.ollama import OllamaEndpointNotFoundError
from config.settings import settings
import asyncio

router = APIRouter()
logger = logging.getLogger(__name__)

class CompletionRequest(BaseModel):
    query: str
    model: str = None

class CompletionResponse(BaseModel):
    response: str

@router.post("/", response_model=CompletionResponse)
async def get_completion(request: CompletionRequest):
    """
    Get a completion from Ollama
    """
    try:
        model = request.model or settings.OLLAMA_MODEL
        if not model.endswith(':latest'):
            model = f"{model}:latest"
            
        # Validate model exists
        if not await validate_ollama_model(model):
            raise HTTPException(
                status_code=404,
                detail=f"Model '{model}' not found. Please make sure the model is installed in Ollama."
            )
            
        llm = get_llm(model)
        chain = CompletionChain(llm)
        try:
            result = await chain.ainvoke({"query": request.query})
            return CompletionResponse(response=result["text"])
        except asyncio.TimeoutError:
            logger.error("Request timed out while waiting for Ollama response", exc_info=True)
            raise HTTPException(
                status_code=504,
                detail="Request timed out while waiting for response. The model may be busy or taking too long to process."
            )
    except OllamaEndpointNotFoundError as e:
        logger.error(f"Ollama endpoint error: {str(e)}", exc_info=True)
        raise HTTPException(
            status_code=503,
            detail="Ollama service is not available. Please make sure Ollama is running and the model is installed."
        )
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error in completion endpoint: {str(e)}", exc_info=True)
        raise HTTPException(
            status_code=500,
            detail=f"Error processing completion request: {str(e)}"
        )
