from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional

class ToolResponse(BaseModel):
    """Response model for tool execution."""
    tool_name: str
    status: str
    result: Any
    error: Optional[str] = None

class ChainResponse(BaseModel):
    """Response model for chain execution."""
    chain_name: str
    result: Any
    metadata: Optional[Dict[str, Any]] = None

class ToolListResponse(BaseModel):
    """Response model for listing available tools."""
    tools: List[Dict[str, str]]

class ErrorResponse(BaseModel):
    """Standard error response."""
    error: str
    detail: Optional[str] = None
