from slap.auth import TokenAuth
from requests_kerberos import HTTPKerberosAuth, OPTIONAL
from slap.auth.types import AuthTypes


def build_auth(auth_type, username=None, password=None, token_url=None, verify_certs=False):
    if auth_type == AuthTypes.TOKEN:
        return TokenAuth(
            username=username,
            password=password,
            token_url=token_url,
            verify_certs=verify_certs
        )
    elif auth_type == AuthTypes.KERBEROS:
        return HTTPKerberosAuth(mutual_authentication=OPTIONAL)
    elif auth_type == AuthTypes.NTLM:
        raise NotImplementedError('NTLM auth is not implemented')
    elif auth_type == AuthTypes.SAML:
        raise NotImplementedError('SAML auth is not implemented')
    else:
        raise KeyError('{} is not a valid auth type'.format(auth_type))
