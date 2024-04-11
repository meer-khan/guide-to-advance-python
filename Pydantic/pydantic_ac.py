import json
from typing import List, Optional
import pydantic 
from icecream import ic
# from beartype.typing import Optional, List

class ISBNMissingError(Exception): 
    def __init__(self, title:str, message:str) -> None:
        self.title = title
        self.message = message
        super().__init__(message)


class ISBN10FormatError(Exception): 
    def __init__(self, value:str, message:str) -> None:
        self.value = value
        self.message = message
        super().__init__(message)


class Book(pydantic.BaseModel):
    title: str
    author: str
    publisher: str
    price: float
    isbn_10: Optional[str]
    isbn_13: Optional[str]
    subtitle: Optional[str]
    # author2: Optional[Author]

    @pydantic.field_validator("isbn_10")
    @classmethod
    def check_ISBN10(cls, value):
        chars = [c for c in value if c in "0123456789Xx"]
        if len(chars) != 10:
            raise ISBN10FormatError(value=value, message="ISBN10 should be 10 digits")
        
        def char_into_int(char:str)->int:
            if char in "Xx":
                return 10
            return int(char)
        
        weighted_sum = sum((10-i) * char_into_int(x) for i,x in enumerate(chars))
        if weighted_sum % 11 != 0:
            raise ISBN10FormatError(value=value, message="ISBN10 digit sum should be divisiable by 11.")
        # return value
    
    # Validation on whole model
    @pydantic.model_validator(mode='before')
    @classmethod
    def check_isb10_or_isbn13(cls,values):
        if "isbn_10" not in values and "isbn_13" not in values: 
            raise ISBNMissingError(title=values['title'], 
                                   message="Document should have either an ISBN10 or ISBN13")
        return values
    
    class Config:
        forzen = False 
        str_to_lower= True

# If validations failed, Pydantics will raise error beautifully 
# try:
#     User(**external_data)  
# except ValidationError as e:
#     print(e.errors())


def main() -> None:
    """Main function."""

    # Read data from a JSON file
    with open("./data.json") as file:
        data = json.load(file)
        # print(data)
        # Priting title
        # print(data[0]["title"])


        books: List[Book] = [Book(**item) for item in data]
        ic(books)
        ic(type(books))
        ic(books[0].title)
        books[0].title = "OK"
        ic(type(books[0]))

        # print(books[0])
        # print(books[0].dict(exclude={"price"}))
        # print(books[1].copy())
        # print(books[1].copy(deep=True))

print("pakistan")



if __name__ == "__main__":
    main()