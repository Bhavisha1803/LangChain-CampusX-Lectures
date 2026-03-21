from langchain_core.prompts import ChatPromptTemplate 

chat_template = ChatPromptTemplate([
    ('system', "You are a helpful {domain} expert that provides concise and accurate answers to user queries."),
    ('human', "explain in simplte terms what is {topic}?")
])

prompt = chat_template.invoke({
    "domain": "AI",
    "topic": "transformer architecture"
})

print(prompt)

#this creates dynamic prompts based on the user input and the template defined. The system message sets the context for the chatbot, while the human message defines the user's query. The invoke method fills in the placeholders with the provided values.