from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatGroq(
    model="llama-3.3-70b-versatile"
    )

prompt1 = PromptTemplate(
    template='give me 5 pointers on {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Generate 2 jokes about {topic}',
    input_variables=['topic']
)

parser = StrOutputParser()

chain = prompt1 | model | parser | prompt2 | model | parser

result = chain.invoke({'topic':'cricket'})

print(result)

chain.get_graph().print_ascii()

