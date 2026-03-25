from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables.base import RunnableSequence, RunnableParallel
from langchain_core.runnables import RunnablePassthrough
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser


load_dotenv()

model = ChatGroq(
    model="llama-3.3-70b-versatile"
    )

parser= StrOutputParser()

prompt1 = PromptTemplate(
    template="Generate a joke about {topic}?",
    input_variables=["topic"]
)
prompt2 = PromptTemplate(
    template="Explain the joke {joke}?",
    input_variables=["joke"]
)

joke_generator_chain = RunnableSequence(prompt1, model, parser)

parallel_chain = RunnableParallel({
    'joke': RunnablePassthrough(),
    'explanation': RunnableSequence(prompt2, model, parser) 
}
)
final_chain = RunnableSequence(joke_generator_chain, parallel_chain)
response = final_chain.invoke({"topic": "anything"})
print(response['joke'])
print(response['explanation'])


