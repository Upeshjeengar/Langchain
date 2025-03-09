from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

llm=ChatAnthropic(model = 'claude-3-5-sonnet-28241022')
result = llm.invoke("what is capital of India") #ask question in invoke

print(result)
