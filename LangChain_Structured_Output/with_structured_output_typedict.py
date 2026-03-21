from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os
from typing import TypedDict, Annotated

load_dotenv()

model = ChatGroq(
    model="llama-3.3-70b-versatile",    
    api_key=os.getenv("GROQ_API_KEY"))  

review = "The movie was fantastic! The plot was engaging and the acting was superb. I highly recommend it to everyone."

#schema
class Review(TypedDict):
    summary: Annotated[str, "A concise summary of the review in one or two sentences"]
    sentiment: str


structured_model = model.with_structured_output(Review)
response = structured_model.invoke(review)
print(response) 
print(response['summary'])
print(response['sentiment'])   