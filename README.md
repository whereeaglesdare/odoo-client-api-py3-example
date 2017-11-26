# Wrapper for odoo web service api #

This is simple implementation for odoo web service api which works on python3.
```python
from client.connector import Connector
conn = Connector(host, database, user, password)
conn.login()
```
## Calling methods ##

For making api calls, use method get_api() and make new instance.
Example of query method: api.<odoo method>.<odoo model>(filters)
```python
api = cursor.get_api()
api.search_count.res.partner([[['is_company', '=', True], ['customer', '=', True]]])
api.search.res.partner([[['is_company', '=', True], ['customer', '=', True]]], {'offset': 10, 'limit': 5})
```

Response:

```python
6
[9, 13, 10, 47, 12, 14]
```