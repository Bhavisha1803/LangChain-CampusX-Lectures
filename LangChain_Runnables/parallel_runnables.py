from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables.base import RunnableSequence, RunnableParallel 
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser


load_dotenv()

model = ChatGroq(
    model="llama-3.3-70b-versatile"
    )

parser= StrOutputParser()

prompt1 = PromptTemplate(
    template="GENERATE A TWEET about {topic}?",
    input_variables=["topic"]
)
prompt2 = PromptTemplate(
    template="GENERATE A LinkedIn post about {topic}?",
    input_variables=["topic"]
)

parallel_chain = RunnableParallel(
    {
        'tweet': RunnableSequence(prompt1, model, parser),
        'linkedin_post': RunnableSequence(prompt2, model, parser)
    }
)

response = parallel_chain.invoke({"topic": "AI"})

#response is a dictionary with keys 'tweet' and 'linkedin_post' and values as the respective outputs from the model for each prompt
print(response['tweet'])
print(response['linkedin_post'])

