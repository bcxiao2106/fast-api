from fastapi import APIRouter
from api.v1.endpoints import tools, chains
from api.v1.endpoints.completion import router as completion_router

api_router = APIRouter()

# Include routers from endpoints
api_router.include_router(tools.router, prefix="/tools", tags=["tools"])
api_router.include_router(chains.router, prefix="/chains", tags=["chains"])
api_router.include_router(completion_router, prefix="/completion", tags=["completion"])
