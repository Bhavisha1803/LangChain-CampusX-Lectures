from langchain_community.document_loaders import TextLoader
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

loader = TextLoader('ai.txt', encoding='utf-8')
docs =loader.load()

response = chain.invoke({'topic': docs[0].page_content})

print(response)

# print(type(docs)) #list
# print(len(docs)) #1 as only 1 doc we loaded
# print(type(docs[0])) #<class 'langchain_core.documents.base.Document'>

# print(docs[0].page_content)
# print(docs[0].metadata)
# #every document has page_content and metadata attributes, page_content is the text content of the document and metadata is a dictionary that can contain any additional information about the document. In this case, metadata contains the source of the document which is 'ai.txt'.



