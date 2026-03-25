from langchain_community.document_loaders import WebBaseLoader, PyPDFLoader
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

loader = WebBaseLoader('https://www.flipkart.com/apple-macbook-air-m5-2026-m5-16-gb-512-gb-ssd-tahoe-mdhe4hn-a/p/itm8505e2f874525?pid=COMHH78YEUAMB68W&lid=LSTCOMHH78YEUAMB68WGNHGES&marketplace=FLIPKART&q=m5+air+macbook&store=6bo%2Fb5g&srno=s_1_1&otracker=AS_QueryStore_OrganicAutoSuggest_1_6_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_6_na_na_na&fm=organic&iid=daa9d882-569f-44eb-a2a0-e627fea30f93.COMHH78YEUAMB68W.SEARCH&ppt=hp&ppn=homepage&ssid=1906jyhjd26z12ww1774466822455&qH=736858c9803c9a4f&ov_redirect=true')
docs = loader.load()

# print(len(docs))
# #gives 1 as it is loading the content of the webpage as a single document, even though the webpage may contain multiple sections or elements, it is treated as a single document by the loader.
# print(docs[0].page_content)

response = chain.invoke({'question': 'What is the price of the product?', 'topic': docs[0].page_content}    )

print(response)