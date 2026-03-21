from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):
    name: str = "akash"
    age: Optional[int] = None #setting none or any other value in optional is mandatory
    email: Optional[EmailStr] = None # EmailStr is a pydantic type that validates email addresses, now optional
    cgpa: Optional[float] = Field(default=None, ge=0.0, le=10.0) #ge and le are used to set the range of values for cgpa, now optional
# new_student = {'name': 32}.  this will throw error as pydantic is used for data validation
new_student = {'name':'bhavisha', "age":25, "email": "bhavisha@example.com", 'cgpa': 8.5}
student = Student(**new_student)

print(student)
print(type(student))

new_student2 = {} #we can specify like this too to fix default values
student2 = Student(**new_student2)
print(student2)


new_student3 = {'name': 'krish', 'age':'21', 'email': 'krish@example.com'}
student3 = Student(**new_student3)
print(student3) #pydantic will try to convert the age to int if possible, if not it will raise an error. In this case it will convert '21' to 21 and print it without any issues.
#pydantic is intelligent enough to handle type conversions when possible, but it will raise errors if the conversion is not possible. For example, if we try to set age to 'twenty', it will raise a validation error because 'twenty' cannot be converted to an integer.


#we can also convert pydantic model to a dictionary using the .dict() method
student_dict = dict(student)
print(student_dict)

#we can also convert pydantic model to json using the .json() method
student_json = student.model_dump_json()
print(student_json)