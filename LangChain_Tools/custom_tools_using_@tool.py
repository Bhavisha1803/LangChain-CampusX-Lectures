from langchain_core.tools import tool

# Step 1 - create a function

def multiply(a, b):
    """Multiply two numbers""" 
    return a*b

# Step 2 - add type hints

def multiply(a: int, b:int) -> int:
    """Multiply two numbers"""
    return a*b

# Step 3 - add tool decorator

@tool
def multiply(a: int, b:int) -> int:
    """Multiply two numbers"""
    return a*b

result = multiply.invoke({"a":3, "b":5})

print(result)
print(multiply.name)
print(multiply.description)
print(multiply.args)
#output
# 15
# multiply
# Multiply two numbers
# {'a': {'title': 'A', 'type': 'integer'}, 'b': {'title': 'B', 'type': 'integer'}}
#multiply is not a function now but a tool and also a runnable with whom llm can interact.

print(multiply.args_schema.model_json_schema())
# {'description': 'Multiply two numbers', 'properties': {'a': {'title': 'A', 'type': 'integer'}, 'b': {'title': 'B', 'type': 'integer'}}, 'required': ['a', 'b'], 'title': 'multiply', 'type': 'object'}
#this is the info that goes to the LLM

