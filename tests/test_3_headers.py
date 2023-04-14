from api.httpbin_api import  http_bin_api
from http import HTTPStatus


def test_list_html():
    res = http_bin_api.list_html()
    assert res.status_code == HTTPStatus.OK
    assert res.headers['Content-Type'] == 'text/html; charset=utf-8'
    assert re.fullmatch(r'', res.json()[''])