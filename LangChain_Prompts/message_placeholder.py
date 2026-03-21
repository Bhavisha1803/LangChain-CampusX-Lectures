from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

#create chat template
chat_template = ChatPromptTemplate([
    ('system', "You are a helpful assistant that provides concise and accurate answers to user queries."),
    MessagesPlaceholder(variable_name="history"),
    ('human', "{query}")
])
#load chat history
chat_history = []
with open("chat_history.txt") as f:
    chat_history.extend(f.readlines())
print(chat_history)


#create prompt
prompt = chat_template.invoke({
    "history": chat_history,
    "query": "Where is my refund?"
})

print(prompt)