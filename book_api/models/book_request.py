from datetime import date, datetime
from pydantic import BaseModel, Field, conint

class newBookReview(BaseModel):
    bookId: str = Field('', example='string', description='Identification number of the book (UUID)', max_length=70)
    review: str = Field('', example='string', description='Review content')
    score: conint(ge=0, le=10) = Field(None, example=1, description='Score of the book from 0 to 10')


class bookReview(BaseModel):
    review: str = Field(None, example='string', description='Review content')
    score: conint(ge=0, le=10) = Field(None, example=1, description='Score of the book from 0 to 10')


if __name__ == '__main__':
    pass

