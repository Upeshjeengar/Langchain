from langchain.output_parsers import JsonOutputParser
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from typing import List, Dict

# Define the JSON schema
class MovieReview(BaseModel):
    title: str
    rating: int
    pros: List[str]
    cons: List[str]

# Create parser
parser = JsonOutputParser(pydantic_object=MovieReview)

# Create prompt template
template = """Review the movie and provide details in JSON format.
Movie: {movie_title}

{format_instructions}
"""

prompt = PromptTemplate(
    template=template,
    input_variables=["movie_title"],
    partial_variables={"format_instructions": parser.get_format_instructions()}
)

# Create chain
model = ChatOpenAI(temperature=0)
chain = prompt | model | parser

# Example usage
try:
    result = chain.invoke({"movie_title": "The Matrix"})
    print("Parsed JSON:", result)
except Exception as e:
    print("Parsing Error:", e) 