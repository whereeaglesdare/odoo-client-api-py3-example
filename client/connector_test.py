import xmlrpc.client

from .connector import Connector

url = 'http://zxcv1.odoo.com'
db = 'zxcv1'
username = 'belokurbogdan@gmail.com'
password = 'DymnaSumish1'


info = xmlrpc.client.ServerProxy('https://demo.odoo.com/start').start()
url, db, username, password = info['host'], info['database'], info['user'], info['password']
print(info)
cursor = Connector(**info)
print(cursor.get_server_info())
print(cursor.login())
