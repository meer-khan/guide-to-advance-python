from pydantic import BaseModel, ValidationError, Field, field_validator, model_validator
from icecream import ic
from typing import Optional
from datetime import date

class Person(BaseModel): 
    first_name : str = Field(strict=False)
    last_name : str = Field(strict=False)
    age: int = Field(strict=False)
    '''
    >> Below operator is not acceptable in python 3.9 it is introduced in python 3.10
    >> OFFICIAL DOC: required, can be None - same as str | None
    '''
    # num: int | None
    # if we want to use Optional in v3.9 or below 3.10 we need to do  
    '''
    OFFICIAL DOC: not required, can be None
    '''
    num2: Optional[int] = None


# it converts string into integer for integer fields but not converts integer into string for string fileds
p1 = Person(first_name="SHAHMEER", last_name="Khan", age="25")

ic(p1)

# Pydantic will cast/convert the data types on it's own if it's convertable

try:
    '''
    It Pydantic v2.5.4 converts string into integer and vice versa on Python 3.11 but in python 3.9 it 
    only converts string into integer but not viceversa.  
    
    '''
    p2 = Person(first_name="F",last_name="N",age="90", num=90 )
    ic(p2)
    ic(type(p2) )


except ValidationError as e:
    # Validation error can also display the error in JSON
    ic(e.json())

'''
NOTE: OFFICIAL DOC- Either .model_dump() or dict(user) will provide a dict of fields, but .model_dump() can take 
                    numerous other arguments. (Note that dict(user) will not recursively convert nested models into dicts, 
                    but .model_dump() will.)
'''

# * Transforming Person class object into python dict 
print("\n1-Transforming Person class object into python dict ")
p1_to_dict = p1.model_dump()
ic(type(p1_to_dict), p1_to_dict)

# * Transforming Person class object into json directly
print("\n2-Transforming Person class object into json directly")
p1_to_json = p1.model_dump_json()
ic(type(p1_to_json), p1_to_json)

# * Excluding some fields, while using model_dump 
print("\n3-Excluding some fields, while using model_dump ")
p1_to_dict = p1.model_dump(exclude=["num2"])
ic(type(p1_to_dict), p1_to_dict)


# * Excluding some fields, while using model_dump_json 
print("\n4-Excluding some fields, while using model_dump ")
p1_to_json = p1.model_dump_json(exclude={"age"}) # In exlude, we can use lists, tuples and sets of values
ic(type(p1_to_json), p1_to_json)



# * Including some fields, while using model_dump 
print("\n5-Including some fields, while using model_dump ")
p1_to_dict = p1.model_dump(include=["first_name"])
ic(type(p1_to_dict), p1_to_dict)


# * Including some fields, while using model_dump_json 
print("\n6-Including some fields, while using model_dump_json ")
p1_to_json = p1.model_dump_json(include=["first_name"], indent=4)
ic(type(p1_to_json), p1_to_json)

# * Creation of another model to understand deserialization 
class Person2(BaseModel): 
    first_name : str
    last_name : str
    dob: date


# Parse Python dictionary and pass it to the Person2 object
# Instructor converted the string formatted date (ISO format) using parse_obj function into python date
# but first, parse_obj is depricated and second model_validate is the latest function 
# and model_validate does not accepts the string formatted date
data = {"first_name": "Muhammad", "last_name": "Khan", "dob": date(1643,1,4)}
p2 = Person2.model_validate(data)
print("\n7- Date Object")
ic(p2)

# *IMPORANT :
# >> For python we create variables in snake case 
# >> But for JSON guide, variables should be in camel case 

# Part - Field
# If we define alias, then we need to pass data with keys of Alias and not the variable name of Person3 class
class Person3(BaseModel): 
    first_name : str = Field(default="M", alias="firstName")
    last_name : str = Field( alias="lastName")
    dob: date = date(1643,1,4)

data = {"first_name": "Muhammad", "lastName": "Khan"}
p3 = Person3.model_validate(data)
print('''\n8- Define Aliases, first_name will be printed as default value "M" becasue, this should
      be written as 'firstName' and lastName is correct in data so it will be printed as "Khan" ''')
ic(p3)

data = {"firstName": "Muhammad"}
'''
As we know, last_name does not has any default value and it's alias is "lastName"
model_validator throw error if we donot pass the lastName and also we can see 
that in error.json, ValidationError of Pydantic is using the aliases instead of variable names
'''
try:
    p3 = Person3.model_validate(data)
    print("\n9- Define Aliases and generate error if we donot pass name key as alias")
    ic(p3)
except ValidationError as e: 
    ic(e.json(indent=1))



data = {"first_name": "Muhammad", "lastName": "Khan"}
p3 = Person3.model_validate(data)
print("\n10- Complete data provided to Person class, in return it will give variable names not aliases")
ic(p3.model_dump())



# PART2 - 
''' We can configure pydantic to allow us to use field/variable names and not aliases 
# becasue it is not a good pythonic practice to pass data as alias to the variable which has 
# different name ''' 

class Person4(BaseModel): 
    first_name : str = Field(default="M", alias="firstName")
    last_name : str = Field( alias="lastName")
    dob: date = date(1643,1,4)
    class Config: 
        populate_by_name = True

# Now I can create data fields, using variable names or aliases, it is upto me
data = {"first_name": "Muhammad", "lastName": "Khan"}
p3 = Person4(firstName="Muhammad", last_name = "Khan")
# p3 = Person4.model_validate(data)
print("\n11- Use variable name or alias doesnot matter")
ic(p3)

# Part3
'''
Using aliases in the return output of model_dump or model_dump_json
'''
data = {"first_name": "Muhammad", "lastName": "Khan"}
p3 = Person4(firstName="Muhammad", last_name = "Khan")
# p3 = Person4.model_validate(data)
print("\n12- Return alias name in deserialization (converting to python dict or json)")
ic(p3.model_dump(by_alias=True))
ic(p3.model_dump_json(by_alias=True)) #This is useful to follow json naming conventions


# Part4
'''Default Behavior, if we pass additional parameter to the Person class, 
it will ignore that vairable'''
data = {"first_name": "Muhammad", "lastName": "Khan"}
p3 = Person4(firstName="Muhammad", last_name = "Khan", junk= "META JUNK")
print("\n13- Removed Extra passed parameters")
ic(p3)


data = {"first_name": "Muhammad", "lastName": "Khan", "junk": "META JUNK"}
p3 = Person4(**data )
print("\n14- Removed Extra passed parameters")
ic(p3)
print(hasattr(p3,"first_name"))
print(hasattr(p3,"junk"))


# Part5 
'''
Allow Extra values 
'''

class Person5(BaseModel): 
    first_name : str = Field(default="M", alias="firstName")
    last_name : str = Field( alias="lastName")
    dob: date = date(1643,1,4)
    class Config: 
        populate_by_name = True
        extra = "allow" # "allow" will allow extra fields, 
                        # "ignore" will ignore extra fields without any error
                        # "forbid" will raise error if extra field is added

                        
data = {"first_name": "Muhammad", "lastName": "Khan", "junk": "META JUNK"}
p5 = Person5(**data )
print("\n15- Added Extra Fields due to configurations of allow extra")
ic(p5)
print(hasattr(p5,"first_name"))
print(hasattr(p5,"junk"))
ic(p5.model_dump())


def snake_to_camel_case(value:str)-> str: 
    if not isinstance(value,str):
        raise ValueError("Value must be string")
    words = value.split("_")
    value = ''.join(word.title() for word in words if word)
    return f"{value[0].lower()}{value[1:]}"



# Part-6
from pydantic import conint, constr
from typing_extensions import Annotated
from pydantic import BaseModel, StringConstraints

class CustomBaseModel(BaseModel):
    class Config: 
        alias_generator = snake_to_camel_case
        extra = "forbid" #Whether to ignore, allow, or forbid extra attributes during model initialization. Defaults to 'ignore'
        populate_by_name = True #Whether an aliased field may be populated by its name as given by the model attribute, as well as the alias. Defaults to False.

class Test(CustomBaseModel): 
    age: conint(gt=0,le=150)
    # last_name: constr(strip_whitespace=True, strict=True,  min_length=2) #strict means, if any datatype that is castable to string but not actually string, throw an error.
    # constr will be deprecated in v3
    last_name: Annotated[str, StringConstraints(strip_whitespace=True, strict=True)]


t = Test(age=1, last_name="          JKJKJ             JKJK              ")
ic(t)


class Test2(CustomBaseModel):
    hash_tag : str

    @field_validator("hash_tag")
    @classmethod
    def validate_hash_tag(cls,value):
        if value.startswith("#"):
            return value 
        return "#"+value
        raise ValueError("hash_tag must start with #")
    
t2 = Test2(hash_tag="OK")
ic(t2)

# PART 7
# class Test3(CustomBaseModel):
#     hash_tag : Annotated[str,StringConstraints(min_length=5)]

#     @field_validator("hash_tag", mode="before")
#     @classmethod
#     def validate_hash_tag(cls,value):
#         if value.startswith("#"):
#             return value 
#         return "#"+value
#         # raise ValueError("hash_tag must start with #")
    
# t3 = Test3(hash_tag="OK")
# ic(t2)

x:str = "90"
# x = 10 
print(x)
print(type(x))