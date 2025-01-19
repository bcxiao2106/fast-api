from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from utils.llm import get_ollama_llm
from chains.completion import CompletionChain

router = APIRouter()

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
        llm = get_ollama_llm(request.model)
        chain = CompletionChain(llm)
        response = await chain.arun(query=request.query)
        return CompletionResponse(response=response)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
