from langchain_core.prompts import PromptTemplate


#designing prompt template 
template = PromptTemplate(
    template ="" \
    "You are a research assistant that provides explanations of research papers in a specified style and length. " \
    "You have to provide summarisation for {paper} research paper. " \
    "The explanation should be in {style} style and should be {length} in length.",
input_variables=["paper", "style", "length"],
validate_template=True
)

template.save("template.json")

