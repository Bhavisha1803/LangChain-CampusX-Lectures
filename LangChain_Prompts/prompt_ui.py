from langchain_groq import ChatGroq 
from dotenv import load_dotenv
import os
import streamlit as st
from langchain_core.prompts import PromptTemplate,load_prompt


load_dotenv()

st.header('research tool')

#user_input = st.text_input('Enter your query here')

paper_input = st.selectbox( "Select Research Paper Name", ["Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"] )

style_input = st.selectbox( "Select Explanation Style", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"] ) 

length_input = st.selectbox( "Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"] )

#designing prompt template 
template = PromptTemplate(
    template ="" \
    "You are a research assistant that provides explanations of research papers in a specified style and length. " \
    "You have to provide summarisation for {paper} research paper. " \
    "The explanation should be in {style} style and should be {length} in length.",
input_variables=["paper", "style", "length"]
)

#filling the prompt template with user inputs
prompt = template.invoke({
    "paper": paper_input,
    "style": style_input,
    "length": length_input
})

model = ChatGroq(
    model="llama-3.3-70b-versatile",    
    api_key=os.getenv("GROQ_API_KEY"))


if st.button('Summarize'):
    result = model.invoke(prompt.to_string())
    st.write(result.content)

