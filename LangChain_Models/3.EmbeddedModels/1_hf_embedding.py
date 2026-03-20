from langchain_huggingface import HuggingFaceEmbeddings
embeddings = HuggingFaceEmbeddings(model="sentence-transformers/all-MiniLM-L6-v2")

text = "Hello, how are you?"
embedding_vector = embeddings.embed_query(text)
print(str(embedding_vector))

docs = ["Hello, how are you?", "What is your name?", "Where are you from?"]
embedding_vectors = embeddings.embed_documents(docs)
print(str(embedding_vectors))