from langchain.prompts import PromptTemplate

# Example prompt templates
GENERAL_PROMPT = PromptTemplate(
    input_variables=["input"],
    template="""
    Instructions: {input}
    
    Response:
    """
)

# Add more prompt templates as needed
