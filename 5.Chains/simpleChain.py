from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

# Initialize HuggingFace model
llm=HuggingFaceEndpoint(
    repo_id = "TinyLlama/TinyLlama-1.1B-Chat-v1.0", #which model you want to use
    task="text-generation" #task of model
)

model = ChatHuggingFace(llm=llm)

prompt = PromptTemplate(
    template="Generate an interesting facts about {topic}",
    input_variables=["topic"]
)

parser = StrOutputParser()

chain = prompt | model | parser

result = chain.invoke({'topic': 'cricket'})

print(result)

chain.get_graph().print_ascii()



''' #OpenAI code
# from langchain_openai import ChatOpenAI
# from dotenv import load_dotenv
# from langchain_core.prompts import PromptTemplate
# from langchain_core.output_parsers import StrOutputParser

# load_dotenv()

# prompt = PromptTemplate(
#     template='Generate 5 interesting facts about {topic}',
#     input_variables=['topic']
# )

# model = ChatOpenAI()

# parser = StrOutputParser()

# chain = prompt | model | parser

# result = chain.invoke({'topic':'cricket'})

# print(result)

# chain.get_graph().print_ascii()
'''