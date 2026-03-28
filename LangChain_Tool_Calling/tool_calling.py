from langchain_groq import ChatGroq
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage
from numpy.ma import product
import requests
from dotenv import load_dotenv
import os

load_dotenv()


# tool create

@tool
def multiply(a: int, b: int) -> int:
  """Given 2 numbers a and b this tool returns their product"""
  return a * b

# print(multiply.invoke({'a':3, 'b':4}))
# print(multiply.name)
# print(multiply.description)
# print(multiply.args)
# 12
# multiply
# Given 2 numbers a and b this tool returns their product
# {'a': {'title': 'A', 'type': 'integer'}, 'b': {'title': 'B', 'type': 'integer'}}


# tool binding

llm =ChatGroq(
    model="llama-3.3-70b-versatile",    
    api_key=os.getenv("GROQ_API_KEY"),
)

llm_with_tools =  llm.bind_tools([multiply])
#now this llm can use the tool to answer questions that require multiplication

# print(llm_with_tools.invoke("Hi how are you?"))
# content="I'm just a language model, so I don't have feelings or emotions like humans do, but I'm here and ready to help with any questions or tasks you might have. How can I assist you today?" additional_kwargs={} response_metadata={'token_usage': {'completion_tokens': 44, 'prompt_tokens': 235, 'total_tokens': 279, 'completion_time': 0.148075091, 'completion_tokens_details': None, 'prompt_time': 0.044036335, 'prompt_tokens_details': None, 'queue_time': 0.171251663, 'total_time': 0.192111426}, 'model_name': 'llama-3.3-70b-versatile', 'system_fingerprint': 'fp_3272ea2d91', 'service_tier': 'on_demand', 'finish_reason': 'stop', 'logprobs': None, 'model_provider': 'groq'} id='lc_run--019d34c2-1e11-7aa0-8ff0-58704a9c38a4-0' tool_calls=[] invalid_tool_calls=[] usage_metadata={'input_tokens': 235, 'output_tokens': 44, 'total_tokens': 279}
#no mention of tools in above output because the question did not require any tools to answer

# print(llm_with_tools.invoke("What is the product of 6 and 7?"))
#content='' additional_kwargs={'tool_calls': [{'id': 'j8xhehfey', 'function': {'arguments': '{"a":6,"b":7}', 'name': 'multiply'}, 'type': 'function'}]} response_metadata={'token_usage': {'completion_tokens': 19, 'prompt_tokens': 241, 'total_tokens': 260, 'completion_time': 0.059088185, 'completion_tokens_details': None, 'prompt_time': 0.087740243, 'prompt_tokens_details': None, 'queue_time': 0.161780824, 'total_time': 0.146828428}, 'model_name': 'llama-3.3-70b-versatile', 'system_fingerprint': 'fp_3272ea2d91', 'service_tier': 'on_demand', 'finish_reason': 'tool_calls', 'logprobs': None, 'model_provider': 'groq'} id='lc_run--019d34c3-45aa-7912-b106-b69111970201-0' 
# tool_calls=[{'name': 'multiply', 'args': {'a': 6, 'b': 7}, 'id': 'j8xhehfey', 'type': 'tool_call'}] invalid_tool_calls=[] usage_metadata={'input_tokens': 241, 'output_tokens': 19, 'total_tokens': 260}
#this ouptut shows that the model recognized that it needed to use the multiply tool to answer the question and made a tool call with the correct arguments. 

#content is empty because llm does not run the tool itself, it just suggests which tool to use and with what arguments. The actual execution of the tool and returning the result is handled by the langchain framework. After the tool is executed, the result would be passed back to the llm to generate a final response to the user.



#tool execution

result = llm_with_tools.invoke("What is the product of 6 and 7?")
tool_call = result.tool_calls[0] #extracting the tool call information from the llm output
arguments = result.tool_calls[0]['args'] #extracting the arguments for the tool call from the llm output
print(multiply.invoke(arguments)) #executing the tool with the extracted arguments
# 42

print(multiply.invoke(tool_call)) #we can also directly pass the tool call information to the tool invoke method and it will extract the arguments and execute the tool
#42
# content='42' name='multiply' tool_call_id='ws14fkdkm'
#it also returned the packaged output with the content, tool name and tool call id which can be useful for tracking and logging purposes.

print(type(multiply.invoke(tool_call)))
#<class 'langchain_core.messages.tool.ToolMessage'>


