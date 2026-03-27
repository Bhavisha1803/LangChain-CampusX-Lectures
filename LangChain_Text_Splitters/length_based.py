from  langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

text = "This is a long text that needs to be split into smaller chunks based on a specified length. The text splitter will ensure that the chunks do not exceed the maximum length while maintaining the integrity of the content. This is useful for processing large documents or preparing text for natural language processing tasks.   The length-based text splitter is a simple yet effective way to manage and organize text data. By specifying the maximum length, you can control how the text is divided, making it easier to work with in various applications. Whether you're dealing with articles, reports, or any other type of text, the length-based splitter can help you break it down into manageable pieces. This approach is particularly beneficial when you need to process text in batches or when you want to ensure that each chunk of text is of a certain size for analysis. The length-based text splitter can be customized to fit your specific needs, allowing you to set the maximum length according to the requirements of your project. Overall, it is a valuable tool for anyone working with large volumes of text data."

splitter = CharacterTextSplitter(
    chunk_size=100, 
    chunk_overlap=0, 
    separator='')
#chunk_overlap is the number of characters that will be repeated at the end of each chunk, it is set to 0 here which means there will be no overlap between chunks, separator is the character that will be used to split the text, it is set to an empty string here which means the text will be split based on the chunk size without any specific separator.
#increasing chunk_overlap can help to maintain context between chunks, but if we increase it more it may cause the chunks to exceed the maximum length, so it is important to find a balance between chunk size and overlap based on the specific use case.
#recommened is 20% of chunk size, so in this case it would be 20 characters of overlap for a chunk size of 100 characters.

result = splitter.split_text(text)

# print(result)

# print("Now printing pdf doc after splitting it using length based splitter")
loader = PyPDFLoader("aipdf.pdf")
docs = loader.load()

pdf_split_response = splitter.split_documents(docs)
# print(pdf_split_response)

# print("checking length\n\n")

# print(len(docs))
# print(len(pdf_split_response))

print(pdf_split_response[0].page_content)