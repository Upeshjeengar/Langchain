from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):

    name: str = 'Upesh'  #setting default value as Upesh
    age: Optional[int] = None #optional field
    email: EmailStr
    cgpa: float = Field(gt=0, lt=10, default=5, description='A decimal value representing the cgpa of the student')
    #setting constraint cgpa should be greater than 0 and less than 10 and default value as 5


new_student = {'age':'32', 'email':'abc@gmail.com'} #will give error if not in specified format unlike typedict

student = Student(**new_student)

print(student)
print(type(student))

student_dict = dict(student)
print(student_dict)

print(student_dict['age'])

student_json = student.model_dump_json()