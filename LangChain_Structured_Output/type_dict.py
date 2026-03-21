from typing import TypedDict

class Person(TypedDict):
    name: str
    age: int

new_person1: Person = { 'age': 30, 'name': 'Alice' }
print(new_person1)

#this works too btw because typedict just tells the type of keys/values a variable should have but not raise errors if thats not followed, its not a rule
new_person2: Person = { 'age': '30', 'name': 'Alice' }
print(new_person2)