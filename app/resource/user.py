from datetime import datetime

from fastapi import APIRouter, Body, Query

from resource import Department, Employee

router = APIRouter(prefix='/user')

@router.post('/update', tags=['User'])
async def update_employment(
        employee: Employee = Body(..., description='employee info'),
        salary: float = Body(..., description='annual salary'),
        department: Department = Body(None, description='department info'),
        add_new: bool = Query(False, description='add new employee if not found'),
        effective_date: datetime = Body(None, description='change effective date, default current date if None')
):
    ...