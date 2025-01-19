from langchain.prompts import PromptTemplate
from chains.base import BaseChain

class CompletionChain(BaseChain):
    """A simple completion chain using Ollama."""
    
    def _create_chain(self):
        prompt = PromptTemplate(
            input_variables=["query"],
            template="Please respond to the following query: {query}"
        )
        return self.llm | prompt
