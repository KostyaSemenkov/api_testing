from http import HTTPStatus

from api.questions_api import api
from utils.assertions import Assert
import re

def test_create():
    name = 'Kostya'
    job = 'Tester'
    id = '2'
    res = api.create(name, job, id)
    assert res.status_code == HTTPStatus.CREATED
    assert res.json()['name'] == name
    assert res.json()['job'] == job
    assert re.fullmatch(r'\d{1,4}',res.json()['id'])
    assert api.delete_user(res.json()['id']).status_code == HTTPStatus.NO_CONTENT


def test_reg():
    email = 'eve.holt@reqres.in'
    password = '123'
    reg = api.registration(email, password)
    reg_body = reg.json()
    assert reg.status_code == HTTPStatus.OK
    Assert.validate_schema(reg_body)


def test_unvalid_reg():
    email = 'eve.holt@reqres.in'
    password = ''
    reg = api.registration(email, password)
    reg_body = reg.json()
    assert reg.status_code == HTTPStatus.BAD_REQUEST
    Assert.validate_schema(reg_body)
    assert  reg_body == {"error": "Missing password"}

