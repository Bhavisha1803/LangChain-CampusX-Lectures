from langchain_community.document_loaders import PyPDFLoader
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate   
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatGroq(
    model="llama-3.3-70b-versatile"
    )

prompt = PromptTemplate(
    template="Generate a summary for {topic}?",
    input_variables=["topic"]
)

parser=StrOutputParser()

chain = prompt | model | parser

loader = PyPDFLoader('aipdf.pdf')
docs = loader.load()

# print(docs)
# print(type(docs)) #list
# print(len(docs))  #4 #number of pages in the pdf, as each page is loaded as a separate document
# print(type(docs[0])) #<class 'langchain_core.documents.base.Document'>
# print(docs[0].page_content) #text content of the first page of the pdf
# print(docs[0].metadata) #metadata of the first page of the pdf, it contains the source of the document which is 'aipdf.pdf' and the page number which is 0 for the first page, 1 for the second page and so on.

chain_response = chain.invoke({'topic': docs[0].page_content})  #we are passing the text content of the first page of the pdf as the topic to the prompt template, which will generate a summary for that page using the language model.
print(chain_response)