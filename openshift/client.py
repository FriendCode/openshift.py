# Python imports
import os

# Libs imports
import requests
from requests.sessions import Session

# Local imports
from openshift.compat import urljoin, urlparse
from openshift.utils import absolute_url

class Openshift(Session):
    __attrs__ = Session.__attrs__ + ['email', 'password', 'token']
    
    def __init__(self, email=None, password=None, token=None):
        super(Openshift, self).__init__()

        self.base_url = "https://openshift.redhat.com/broker/rest/"
        self.email = email
        self.password = password
        self.token = token
        

    def _set_url(self, url):
        if not absolute_url(url):
            return urljoin(self.base_url, url)
        return url

    def request(self, method, url, bearer_auth=True, **req_kwargs):
        '''
        A loose wrapper around Requests' :class:`~requests.sessions.Session`

        :param method: A string representation of the HTTP method to be used.
        :type method: str
        :param url: The resource to be requested.
        :type url: str
        :param bearer_auth: Whether to use Bearer Authentication or not,
            defaults to `True`.
        :type bearer_auth: bool
        :param \*\*req_kwargs: Keyworded args to be passed down to Requests.
        :type \*\*req_kwargs: dict
        '''
        url = self._set_url(url)

        if self.token is None:
            req_kwargs["auth"] = (self.email, self.password)
        else:
            req_kwargs['headers'] = {"Authorization": "Bearer %s" % self.token}

        return super(Openshift, self).request(method, url, **req_kwargs)

    def add_authorization(self, scope="session"):
        '''
        Add a temporary authorization to an account and adapt the token for this

        :param Scope for this authorization
        '''
        r = self.post("user/authorizations", data={
            "scope": scope
        })
        r.raise_for_status()
        data = r.json()
        self.token = data['data']['token']

        return data['data']

    def get_user(self):
        '''
        Return user informations
        '''
        r = self.get("user")
        r.raise_for_status()
        data = r.json()

        return data['data']

    def add_sshkey(self, name=None, content=None, keytype="ssh-rsa"):
        '''
        Add a new ssh key

        :param name Name of key
        :param content The key portion (excluding ssh-rsa and comment)
        :param keytype Type of SSH key (default "ssh-rsa")
        '''
        r = self.post("user/keys", data={
            "name": name,
            "content": content,
            "type": keytype
        })
        r.raise_for_status()
        data = r.json()

        return data['data']





    