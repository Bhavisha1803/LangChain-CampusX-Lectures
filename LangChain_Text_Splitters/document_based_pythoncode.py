#same as recursive but it uses different separators to split the text, it will try to split using class def keywords in python code, for markdown it may use headings as separators
#used where docs donthave simple structure like paragraphs or sentences, for example code files, markdown files etc. it is a more intelligent way to split the text while maintaining the context and coherence of the content.
from langchain_text_splitters import Language, RecursiveCharacterTextSplitter

text = "" \
"class Student:\n" \
"    def __init__(self, name, age):\n" \
"        self.name = name\n" \
"        self.age = age\n" \
"\n" \
"    def get_details(self):\n" \
"        return f'Name: {self.name}, Age: {self.age}'\n" \
"\n"

splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,
    chunk_size=100,
    chunk_overlap=0
)
result =splitter.split_text(text)
print(result)
print('\n len(result) \n')
print(len(result))
