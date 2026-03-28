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



# tool binding

llm =ChatGroq(
    model="llama-3.3-70b-versatile",    
    api_key=os.getenv("GROQ_API_KEY"),
)

llm_with_tools =  llm.bind_tools([multiply])

#tool execution

messages = []
query = HumanMessage(content="What is the product of 6 and 7?")
messages.append(query)
#at this point messages has onlu Human Message

result = llm_with_tools.invoke(messages)
messages.append(result)
#at this point messages has the Human Message and the LLM response which includes the tool call information but not the actual result of the tool execution

tool_call = result.tool_calls[0]
tool_result = multiply.invoke(tool_call)
messages.append(tool_result)
#at this point messages has the Human Message, the LLM response with tool call information and the actual result of the tool execution. 



# Now we can pass all these messages back to the llm to generate a final response to the user that includes the result of the tool execution.
final_response = llm_with_tools.invoke(messages)

print(final_response.content)
# The product of 6 and 7 is 42.

print(final_response)
#content='The product of 6 and 7 is 42.' additional_kwargs={} response_metadata={'token_usage': {'completion_tokens': 13, 'prompt_tokens': 271, 'total_tokens': 284, 'completion_time': 0.031828716, 'completion_tokens_details': None, 'prompt_time': 0.078379921, 'prompt_tokens_details': None, 'queue_time': 0.056690148, 'total_time': 0.110208637}, 'model_name': 'llama-3.3-70b-versatile', 'system_fingerprint': 'fp_68f543a7cc', 'service_tier': 'on_demand', 'finish_reason': 'stop', 'logprobs': None, 'model_provider': 'groq'} id='lc_run--019d34d7-bb93-7c83-8f35-7ef1e35a77a1-0' tool_calls=[] invalid_tool_calls=[] usage_metadata={'input_tokens': 271, 'output_tokens': 13, 'total_tokens': 284}