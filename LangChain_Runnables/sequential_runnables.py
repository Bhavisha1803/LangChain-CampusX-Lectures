from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables.base import RunnableSequence 
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser


load_dotenv()

model = ChatGroq(
    model="llama-3.3-70b-versatile"
    )

prompt1 = PromptTemplate(
    template="Write a joke on {topic}?",
    input_variables=["topic"]
)
prompt2 = PromptTemplate(
    template="Explain the joke {joke}?",
    input_variables=["joke"]
)


parser = StrOutputParser()

chain = RunnableSequence(prompt1,model,parser,prompt2,model,parser)

response = chain.invoke({"topic": "food"})

print(response)

