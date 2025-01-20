from langchain.chains import LLMChain
from langchain.llms.base import BaseLLM

class BaseChain:
    """Base class for custom chains."""
    
    def __init__(self, llm: BaseLLM):
        self.llm = llm
        self.chain = self._create_chain()
    
    def _create_chain(self) -> LLMChain:
        """Create the chain."""
        raise NotImplementedError("Subclass must implement abstract method")
    
    async def ainvoke(self, inputs: dict):
        """Run the chain asynchronously."""
        return await self.chain.ainvoke(inputs)
    
    def invoke(self, inputs: dict):
        """Run the chain."""
        return self.chain.invoke(inputs)
