from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

llm=ChatGoogleGenerativeAI(model = 'gemini-1.5-pro')
result = llm.invoke("what is capital of India") #ask question in invoke

print(result)
print(result.content)
