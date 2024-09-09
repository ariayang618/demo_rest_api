from test import client


def test_employment_update():
    employee = {
        "name": "John Smith",
        "dob": "1988-08-08",
        "user_id": "jsmith",
        "nationality": "USA"
    }
    unit =  {
        "name": "research",
        "location": {
            "number": 234,
            "street": "Main St",
            "city": "Saratoga Springs",
            "state": "NY",
            "zip": "12866"
        }
    }
    employment = {
        "employee": employee,
        "effective_date": "2025-12-25",
        "salary": "88000",
        "department": unit
    }
    res = client.post('/user/update/employment', json=employment)
    assert res.status_code == 400 and res.json()['detail']['error'] == 'user_id "jsmith" is not found'
    res = client.post('/user/update/employment', json=employment, params={'add_new': True})
    assert res.status_code == 200 and res.json()['status'] == 'updated'
    res = client.get('/user/jsmith0/employment')
    assert res.status_code == 400 and res.json()['detail']['error'] == 'user "jsmith0" is not found'
    res = client.get('/user/jsmith/employment')
    assert res.status_code == 200 and len(h := res.json()['history']) == 1 and h[0]['salary'] == 88000
    employment['salary'] = 108800
    employment['effective_date'] = '2025-12-28'
    res = client.post('/user/update/employment', json=employment)
    assert res.status_code == 200
    res = client.get('/user/jsmith/employment')
    assert res.status_code == 200 and len(h := res.json()['history']) == 2 and h[1]['salary'] == 108800