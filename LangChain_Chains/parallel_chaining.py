from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel

load_dotenv()

model1 = ChatGroq(
    model="llama-3.3-70b-versatile"
    )

model2 = ChatGroq(
    model="llama-3.3-70b-versatile"
)

prompt1 = PromptTemplate(
    template='generate short and simple notes from the following text: {text}',
    input_variables=['text']
)

prompt2 = PromptTemplate(
    template='generate 5 quizz questions from the following text: {text}',
    input_variables=['text']
)

prompt3 = PromptTemplate(
    template='merge the following notes and quiz into single document: {notes} and {quiz}',
    input_variables=['notes', 'quiz']
)

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    'notes': prompt1 | model1 | parser,
    'quiz': prompt2 | model2 | parser
})

merge_chain = prompt3 | model1 | parser

chain = parallel_chain | merge_chain

result = chain.invoke("Cricket")

print(result)

chain.get_graph().print_ascii()