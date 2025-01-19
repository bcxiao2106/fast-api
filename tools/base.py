from langchain.tools import BaseTool
from pydantic import BaseModel

class CustomTool(BaseTool):
    """Base class for custom tools."""
    name: str = ""
    description: str = ""
    
    def _run(self, query: str) -> str:
        """Use the tool."""
        raise NotImplementedError("Subclass must implement abstract method")
    
    async def _arun(self, query: str) -> str:
        """Use the tool asynchronously."""
        raise NotImplementedError("Subclass must implement abstract method")
