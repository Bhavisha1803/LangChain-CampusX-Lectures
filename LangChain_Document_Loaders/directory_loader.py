from langchain_community.document_loaders import DirectoryLoader, TextLoader, PyPDFLoader
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

loader = DirectoryLoader('folder_of_files', 
                         glob='**/*.txt'
) #we can specify the glob pattern to load only specific types of files, in this case we are loading all the txt files in the data directory and its subdirectories.

doc = loader.lazy_load()
#we use lazy_load() method to load the documents lazily, which means that the documents will be loaded one by one when we iterate over them, instead of loading all the documents at once in memory. This is useful when we have a large number of documents and we want to avoid loading them all at once in memory.
#it returns a generator object which we can iterate over to get the documents one by one.


print(len(doc))