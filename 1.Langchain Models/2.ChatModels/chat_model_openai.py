from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model = 'gpt-4')
result = model.invoke("what is capital of India") #ask question in invoke

print(result) #output is a metadata(dictionary type) rather than direct answer as was in LLM
print(result.content) #this will print answer like LLM

#you can also control randomness(creativity) of language model's output using temperature parameter
# lower values(0-0.3)- more deterministic and predictable
# higher values(0.7-1.5)-more random, creative diverse

model_1=ChatOpenAI(model='gpt-4', temperature=1.8 , max_completion_tokens=10)
# max_completion_tokens=Number of tokens will be generated