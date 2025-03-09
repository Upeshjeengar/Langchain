from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm=HuggingFaceEndpoint(
    repo_id = "TinyLlama/TinyLlama-1.1B-Chat-v1.0", #which model you want to use
    task="text-generation" #task of model
)
model = ChatHuggingFace(llm=llm)
result = model.invoke("what is capital of India") #ask question in invoke

print(result.content) #print the answer