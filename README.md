# Wrapper for odoo web service api #

This is simple implementation for odoo web service api which works on python3.
```python
from client.connector import Connector
conn = Connector(host, database, user, password)
conn.login()
```