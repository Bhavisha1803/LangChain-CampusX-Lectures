from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()

model = ChatGroq(
    model="llama-3.3-70b-versatile",    
    api_key=os.getenv("GROQ_API_KEY"))  

messages = [
    SystemMessage(content="You are a helpful assistant that provides concise and accurate answers to user queries."),
    HumanMessage(content="What is the capital of France?"),
]

response = model.invoke(messages)
messages.append(AIMessage(content=response.content))
print(messages)