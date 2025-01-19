from pydantic import BaseModel, Field
from typing import Dict, Any, Optional

class ToolRequest(BaseModel):
    """Request model for tool execution."""
    tool_name: str = Field(..., description="Name of the tool to execute")
    parameters: Dict[str, Any] = Field(default_factory=dict, description="Parameters for the tool")

class ChainRequest(BaseModel):
    """Request model for chain execution."""
    chain_name: str = Field(..., description="Name of the chain to execute")
    inputs: Dict[str, Any] = Field(..., description="Inputs for the chain")
    
class QueryRequest(BaseModel):
    """Request model for general queries."""
    query: str = Field(..., description="Query text")
    model: Optional[str] = Field(default="gpt-3.5-turbo", description="Model to use")
    temperature: Optional[float] = Field(default=0.7, description="Temperature for generation")
