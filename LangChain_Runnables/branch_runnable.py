from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables.base import RunnableSequence, RunnableParallel
from langchain_core.runnables import RunnablePassthrough, RunnableBranch
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser


load_dotenv()

model = ChatGroq(
    model="llama-3.3-70b-versatile"
    )

parser= StrOutputParser()

prompt1 = PromptTemplate(
    template="Generate a report about {topic}?",
    input_variables=["topic"]
)

report_generator_chain = RunnableSequence(prompt1, model, parser)    

prompt2 = PromptTemplate(
    template="Summarize the report: {report}?",
    input_variables=["report"]
)

summarizer_chain = RunnableSequence(prompt2, model, parser)

branch_chain = RunnableBranch(
    ((lambda x: len(x.split()) > 500), summarizer_chain),
    RunnablePassthrough()
)

final_chain = RunnableSequence(report_generator_chain, branch_chain)

response = final_chain.invoke({"topic": "AI"})
print(response)