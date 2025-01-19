from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.llms.base import BaseLLM

class BaseChain:
    """Base class for custom chains."""
    
    def __init__(self, llm: BaseLLM):
        self.llm = llm
        self.chain = self._create_chain()
    
    def _create_chain(self) -> LLMChain:
        """Create the chain."""
        raise NotImplementedError("Subclass must implement abstract method")
    
    async def arun(self, **kwargs):
        """Run the chain asynchronously."""
        return await self.chain.arun(**kwargs)
    
    def run(self, **kwargs):
        """Run the chain."""
        return self.chain.run(**kwargs)
