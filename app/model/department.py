from model import BaseModel
from resource import Location


class Department(BaseModel):
    def __init__(self, name: str, location: Location):
        self.name = name
        self.location = location
        self.id = 0
        self.location_id = 0

    def get_id(self):
        res, err = self.fetch(f"select id from department where name = '{self.name}' and location_id = {self.location_id}")
        if err:
            ...
        elif res:
            self.id = res[0][0]
        return self.id

    def get_location_id(self):
        sql = f'''
            select id from location 
            where (number, street, zip) in (({self.location.number}, '{self.location.street}', '{self.location.zip}'))
        '''
        res, err = self.fetch(sql)
        if err:
            ...
        elif res:
            self.location_id = res[0][0]
        return self.location_id