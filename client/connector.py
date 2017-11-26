import xmlrpc.client
from socket import gethostbyname, gaierror


class Connector(object):

    def __init__(self, host, database, user, password):
        self._url = host
        self._db = database
        self._username = user
        self._password = password
        self._common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(self._url))

    def get_server_info(self):
        try:
            response = self._common.version()
            return response
        except gaierror:
            return False

    def login(self):
        if self.get_server_info():
            try:
                uid = self._common.authenticate(self._db, self._username, self._password, {})
                return True
            except xmlrpc.client.Fault:
                return False
        else:
            return False





