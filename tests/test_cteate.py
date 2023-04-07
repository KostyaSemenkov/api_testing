from http import HTTPStatus

from api.questions_api import api


def test_create():
    name = 'Kostya'
    job = 'Tester'
    res = api.create(name,job)
    assert res.status_code == HTTPStatus.CREATED
    assert res.json()['name'] == name
    assert res.json()['job'] == job
    assert api.delete_user(res.json()['id']).status_code == HTTPStatus.NO_CONTENT