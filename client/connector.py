import xmlrpc.client
from socket import gethostbyname, gaierror


class Connector(object):

    def __init__(self, host, database, user, password):
        self._url = host
        self._db = database
        self._username = user
        self._password = password
        self._common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(self._url))
        self._uid = None
        self._models = None

    def get_server_info(self):
        try:
            response = self._common.version()
            return response
        except gaierror:
            return False

    def login(self):
        if self.get_server_info():
            try:
                self._uid = self._common.authenticate(self._db, self._username, self._password, {})
                self._models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(self._url))
                return self._uid
            except xmlrpc.client.Fault as e:
                print(str(e))
                return False
        else:
            return False

    def get_api(self):
        return ApiMethod(self)

    def execute(self, model_method, values=None):
        attrs = model_method.split('.')
        if self._uid:
            return self._models.execute_kw(self._db, self._uid, self._password,
                                           attrs[1] if len(attrs) == 2 else ''.join(attrs[1] + '.' + attrs[2]),
                                           attrs[0], [[['is_company', '=', True], ['customer', '=', True]]])
        else:
            return 'You should auth before use api methods'


class ApiMethod(object):

    __slots__ = ('_model', '_method', '_conn')

    def __init__(self, conn, method=None):

        self._conn = conn
        self._method = method

    def __getattr__(self, method):
        return ApiMethod(self._conn, (self._method + '.' if self._method else '') + method)

    def __call__(self, **kwargs):
        return self._conn.execute(self._method, kwargs)


