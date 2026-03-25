from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables.base import RunnableSequence, RunnableParallel, RunnableLambda
from dotenv import load_dotenv
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser


load_dotenv()

model = ChatGroq(
    model="llama-3.3-70b-versatile"
    )

parser= StrOutputParser()

prompt1 = PromptTemplate(
    template="Write a joke on {topic}?",
    input_variables=["topic"]
)
joke_generator_chain = RunnableSequence(prompt1, model, parser) 

def count_words(inputs):
    word_count = len(inputs.split())
    return word_count

parallel_chain = RunnableParallel({
    'joke': RunnablePassthrough(),
    'count_words': RunnableLambda(lambda inputs: count_words(inputs))
})

final_chain = RunnableSequence(joke_generator_chain, parallel_chain)

response = final_chain.invoke({"topic": "anything"})

print(response['joke'])
print(response['count_words'])