from langchain_core.tools import tool
from langchain_core.tools import InjectedToolArg
from typing import Annotated
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
import os
import requests

load_dotenv()

@tool
def get_conversion_factor(base_currency: str, target_currency: str) -> float:
  """
  This function fetches the currency conversion factor between a given base currency and a target currency
  """
  url = f'https://v6.exchangerate-api.com/v6/c754eab14ffab33112e380ca/pair/{base_currency}/{target_currency}'

  response = requests.get(url)

  return response.json()

@tool
def convert(base_currency_value: int, conversion_rate: Annotated[float, InjectedToolArg]) -> float:
  """
  given a currency conversion rate this function calculates the target currency value from a given base currency value
  """

  return base_currency_value * conversion_rate

#print(get_conversion_factor.invoke({'base_currency': 'USD', 'target_currency': 'INR'}))
#{'result': 'success', 'documentation': 'https://www.exchangerate-api.com/docs', 'terms_of_use': 'https://www.exchangerate-api.com/terms', 'time_last_update_unix': 1774656001, 'time_last_update_utc': 'Sat, 28 Mar 2026 00:00:01 +0000', 'time_next_update_unix': 1774742401, 'time_next_update_utc': 'Sun, 29 Mar 2026 00:00:01 +0000', 'base_code': 'USD', 'target_code': 'INR', 'conversion_rate': 94.8347}

# print(convert.invoke({'base_currency_value': 100, 'conversion_rate': 94.8347}))
#9483.47

# tool binding
llm =ChatGroq(
    model="llama-3.3-70b-versatile",    
    api_key=os.getenv("GROQ_API_KEY"),
)

llm_with_tools =  llm.bind_tools([get_conversion_factor, convert])

#tool calling

messages = [HumanMessage('What is the conversion factor between INR and USD, and based on that can you convert 10 inr to usd')]
ai_message = llm_with_tools.invoke(messages)
messages.append(ai_message) 

#print(ai_message.tool_calls) #extracting the tool call information from the llm output
# [{'name': 'get_conversion_factor', 'args': {'base_currency': 'INR', 'target_currency': 'USD'}, 'id': 'k30bjamys', 'type': 'tool_call'}, {'name': 'convert', 'args': {'base_currency_value': 10}, 'id': 'ac9wmt97j', 'type': 'tool_call'}]

# for tool_call in ai_message.tool_calls:
#   print(tool_call)

import json

for tool_call in ai_message.tool_calls:
  # execute the 1st tool and get the value of conversion rate
  if tool_call['name'] == 'get_conversion_factor':
    tool_message1 = get_conversion_factor.invoke(tool_call)
    # fetch this conversion rate
    conversion_rate = json.loads(tool_message1.content)['conversion_rate']
    # append this tool message to messages list
    messages.append(tool_message1)
  # execute the 2nd tool using the conversion rate from tool 1
  if tool_call['name'] == 'convert':
    # fetch the current arg
    tool_call['args']['conversion_rate'] = conversion_rate
    tool_message2 = convert.invoke(tool_call)
    messages.append(tool_message2)

final_response = llm_with_tools.invoke(messages)
print(final_response.content)