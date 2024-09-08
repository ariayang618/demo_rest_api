from datetime import datetime

from pydantic import BaseModel, Field


class Address(BaseModel):
    number: int = Field(..., description='street number')
    street: str = Field(..., description='street name')
    city: str = Field(..., description='city name')
    state: str = Field(..., description='state code', pattern=r'[A-Z]{2}')
    zip: str = Field(..., description='zip code', pattern=r'\d{5}')


class Employee(BaseModel):
    name: str = Field(..., description='employee name')
    dob: datetime = Field(..., description='date of birth in yyyy-mm-dd format', pattern=r'[0-9]{4}-[0-9]{2}-[0-9]{2}', examples=['2018-06-18'])
    user_id: str = Field(..., description='unique company AD user id', pattern=r'[a-z0-9]{3,8}')
    nationality: str = Field(..., description='employee citizenship')


class Department(BaseModel):
    name: str = Field(..., description='department name', pattern=r'[a-z\s]+')
    address: Address = Field(..., description='office location')
