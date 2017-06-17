import requests
from requests.auth import AuthBase

from slap.api import parse_response


class TokenAuth(AuthBase):
    def __init__(self, username, password, token_url):
        self._token_url = token_url
        self._username = username
        self._password = password

    def __call__(self, r):
        r.params['token'] = self._get_token()
        return r

    def _get_token(self):
        params = {
            'username': self._username,
            'password': self._password,
            'client': 'requestip',
            'expiration': 60,
            'f': 'json'
        }
        response = requests.post(self._token_url, params)
        parsed_response = parse_response(response)
        return parsed_response['token']
