from api.httpbin_api import http_bin_api

from http import HTTPStatus


def test_time_out():
    assert http_bin_api.time_out(4).status_code == HTTPStatus.OK

