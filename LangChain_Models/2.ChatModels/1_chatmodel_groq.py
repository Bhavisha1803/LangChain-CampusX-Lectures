from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()

chatModel =ChatGroq(
    model="llama-3.3-70b-versatile",    
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=1.7, 
    max_tokens=200
)
result=chatModel.invoke("top 3 restaurants in New York?")
print(result.content)
