from datetime import date

from fastapi import APIRouter, Body, Query, Path

from common import abort_with_error
from model.user import User
from model.department import Department as Unit
from resource import Department, Employee, StatusUpdate, Error, doc_update_employment

router = APIRouter(prefix='/user')

@router.post('/update/employment', tags=['User'], description=doc_update_employment,
             response_model=StatusUpdate,
             responses={400: {'model': Error, 'description': ['invalid request - department / location not found']}}
)
async def update_employment(
        employee: Employee = Body(..., description='employee info'),
        salary: float = Body(..., description='annual salary'),
        department: Department = Body(None, description='department info'),
        add_new: bool = Query(False, description='add new employee if not found'),
        effective_date: date = Body(None, description='change effective date, default current date if None')
):
    user = User(name=employee.name, user_id=employee.user_id, dob=employee.dob, nationality=employee.nationality)
    unit = Unit(name=department.name, location=department.location)
    if unit.get_location_id() == 0:
        abort_with_error(f'location "{department.location}" not found', 400)
    if unit.get_id() == 0:
        abort_with_error(f'no department "{unit.name}" is found at location: "{unit.location}"', 400)
    if user.get_id() == 0 and not add_new:
        abort_with_error(f'user_id "{employee.user_id}" is not found', 400)
    if not user.is_existing and (err := user.add_new()):
        abort_with_error(err, 500)
    if err := user.update(unit.location_id, salary, effective_date):
        abort_with_error(f'fail to update employment for {user.user_id}: {err}', 500)
    return {'status': 'updated'}


@router.get('/{user_id}/employment', tags=['User'], description='get employment history for a given user')
async def get_user_employment_history(
        user_id: str = Path(..., description='user unique ID', pattern=r'[a-z0-9]{3,8}')
):
    user = User(user_id=user_id)
    if user.get_id() == 0:
        abort_with_error(f'user "{user_id}" is not found', 400)
    res, err = user.get_employment_history()
    return {'history': [dict(zip(('date', 'salary', 'unit', 'address'), r)) for r in res]}
