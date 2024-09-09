from datetime import date

from pydantic import BaseModel, Field

doc_update_employment = '''
#### update employment history for an employee
- use `add_new` flag to add a new user if not found
- location and department must be available to update employment history
- salary / location / department are field to update on a specific date
'''


class Location(BaseModel):
    number: int = Field(..., description='street number')
    street: str = Field(..., description='street name')
    city: str = Field(..., description='city name')
    state: str = Field(..., description='state code', pattern=r'[A-Z]{2}')
    zip: str = Field(..., description='zip code', pattern=r'\d{5}')


class Employee(BaseModel):
    name: str = Field(..., description='employee name')
    dob: date = Field(..., description='date of birth in yyyy-mm-dd format', examples=['2018-06-18'])
    user_id: str = Field(..., description='unique company AD user id', pattern=r'[a-z0-9]{3,8}')
    nationality: str = Field(..., description='employee citizenship')


class Department(BaseModel):
    name: str = Field(..., description='department name', pattern=r'[a-z\s]+')
    location: Location = Field(..., description='office location')


class StatusUpdate(BaseModel):
    status: str = Field(..., description='update status')

class Error(BaseModel):
    status_code: int = Field(..., description='http status code')
    message: str = Field(..., description='error message')