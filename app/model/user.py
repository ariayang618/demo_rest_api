from datetime import date

from common import logger
from model import BaseModel


class User(BaseModel):
    def __init__(self, user_id, name=None, dob: date = None, nationality = None):
        self.name = name
        self.user_id = user_id
        self.dob = dob
        self.nationality = nationality
        self.id = 0

    @property
    def is_existing(self):
        return self.id > 0

    def get_id(self):
        res, err = self.fetch(f"select id from employee where user_id = '{self.user_id}'")
        if err:
            ...
        elif res:
            self.id = res[0][0]
        return self.id

    def add_new(self):
        logger.info(f'adding new user for: {self.name}')
        sql = f'''
            insert into employee (user_id, name, dob, nationality) values 
            ('{self.user_id}', '{self.name}', '{self.dob.strftime("%Y-%m-%d")}', '{self.nationality}')
        '''
        self.id, err = self.sql_insert(sql)
        if err:
            logger.info(e_ := f'fail to add new user for {self.user_id}: {err}')
            return e_
        else:
            logger.info(f'new user added for {self.user_id} with id: {self.id}')
            return ''

    def update(self, location_id, salary, start_date: date):
        sql = f'''
            insert into employment (employee_id, department_id, salary, effective_date) values
            ({self.id}, {location_id}, {salary}, '{start_date.strftime('%Y-%m-%d')}')
        '''
        id_, err = self.sql_insert(sql)
        if id_:
            logger.info(f'successfully update employment history for user: {self.user_id}')
        return err

    def get_employment_history(self):
        sql = f'''
            select em.effective_date, em.salary, d.name as department, 
                concat(l.number, ' ', l.street, ', ', l.zip) as address
            from employee e 
            join employment em on e.id = em.employee_id
            join department d on d.id = em.department_id
            join location l on l.id = d.location_id
            where e.user_id = '{self.user_id}'
            order by em.effective_date
        '''
        return self.fetch(sql)

