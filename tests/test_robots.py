from api.httpbin_api import http_bin_api
import re
from http import HTTPStatus
from utils.assertions import Assert

# def test_robots():
#     res = http_bin_api.robots()
#     assert res.status_code == HTTPStatus.OK
#     assert res.headers['Content-Type'] == 'text/plain'
#     assert re.fullmatch(r".*User-agent:\*.*Disallow:/deny.*", res.text, flags=re.DOTALL)


def test_ip():
    res = http_bin_api.ip()
    assert res.status_code == HTTPStatus.OK
    if res.headers['content-type'] == 'application/json':
        Assert.validate_schema(res.json())
        num = res.json()['origin']
        assert re.fullmatch(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", num)


