import requests


class Client:
    @staticmethod
    def get(url):
        return requests.request('Get', url)
