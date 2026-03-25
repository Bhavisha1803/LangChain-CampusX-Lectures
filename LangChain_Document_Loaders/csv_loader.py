from langchain_community.document_loaders import CSVLoader
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate   
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatGroq(
    model="llama-3.3-70b-versatile"
    )

prompt = PromptTemplate(
    template="Answer the question {question} about {topic}",
    input_variables=["question","topic"]
)

parser=StrOutputParser()

chain = prompt | model | parser

loader = CSVLoader(file_path="./currency.csv")
documents = loader.load()

print(len(documents)) #output 163 as there are 163 rows in the csv file
print(documents[51])  
#page_content='Code: GHS
# Symbol: ₵
# Name: Ghana cedi' metadata={'source': './currency.csv', 'row': 51}
print(type(documents[51])) #output <class 'langchain_core.document.Document'>, as the loader returns a list of Document objects