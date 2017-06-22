from unittest import TestCase
from mock import patch

from requests_kerberos import OPTIONAL

from slap.auth.factory import build_auth
from slap.auth.types import AuthTypes



class TestAuthFactory(TestCase):

    def test_builds_token_auth(self):
        with patch('slap.auth.factory.TokenAuth') as mock:
            username = 'user'
            password = 'password'
            token_url = 'getToken'
            build_auth(AuthTypes.TOKEN, username=username, password=password, token_url=token_url)
            mock.assert_called_once_with(
                username=username,
                password=password,
                token_url=token_url,
                verify_certs=False
            )

    def test_builds_kerberos_auth(self):
        with patch('slap.auth.factory.HTTPKerberosAuth') as mock:
            build_auth(AuthTypes.KERBEROS)
            mock.assert_called_once_with(mutual_authentication=OPTIONAL)