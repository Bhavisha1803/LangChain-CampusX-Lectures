from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from dotenv import load_dotenv
import os

load_dotenv()

model = ChatGroq(
    model="llama-3.3-70b-versatile",    
    api_key=os.getenv("GROQ_API_KEY"))

chat_history = [
    SystemMessage(content="You are a helpful assistant that provides concise and accurate answers to user queries."),
]

while True:
    user_input = input("You: ")
    chat_history.append(HumanMessage(content=user_input))
    if user_input.lower() in ["exit", "quit"]:
        print("Exiting chatbot. Goodbye!")
        break

    response = model.invoke(chat_history)
    chat_history.append(AIMessage(content=response.content))
    print(f"Chatbot: {response.content}")
    
print(chat_history)