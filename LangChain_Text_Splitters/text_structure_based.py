from langchain_text_splitters import RecursiveCharacterTextSplitter

text = "This is a long text that needs to be split into smaller chunks based on a specified length. The text splitter will ensure that the chunks do not exceed the maximum length while maintaining the integrity of the content. This is useful for processing large documents or preparing text for natural language processing tasks.   The length-based text splitter is a simple yet effective way to manage and organize text data. By specifying the maximum length, you can control how the text is divided, making it easier to work with in various applications. Whether you're dealing with articles, reports, or any other type of text, the length-based splitter can help you break it down into manageable pieces. This approach is particularly beneficial when you need to process text in batches or when you want to ensure that each chunk of text is of a certain size for analysis. The length-based text splitter can be customized to fit your specific needs, allowing you to set the maximum length according to the requirements of your project. Overall, it is a valuable tool for anyone working with large volumes of text data."

splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=0
)
result = splitter.split_text(text)
print(result)
print('\n len(result) \n')
print(len(result))

#recursive character text splitter will try to split the text based on the specified chunk size and overlap, but it will also try to split the text at natural break points such as sentences or paragraphs to maintain the integrity of the content. This can help to ensure that the chunks are more coherent and easier to understand, especially when dealing with longer texts. The recursive character text splitter is a more advanced version of the length-based splitter that takes into account the structure of the text while splitting it into chunks.
#first paragraph \n\n then lines \n then spaces " " then it goes to character level if it still exceeds the chunk size, so it is a more intelligent way to split the text while maintaining the context and coherence of the content.