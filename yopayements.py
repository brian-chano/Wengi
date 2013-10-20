# -*- coding: utf-8 -*-

import requests

url = 'https://41.220.12.206/services/yopaymentsdev/task.php'

xml = """<?xml version="1.0" encoding="UTF-8"?>
<AutoCreate>
	<Request>
		<APIUsername>90006220115</APIUsername>
		<APIPassword>1288923456</APIPassword>
		<Method>acacctbalance</Method>
	</Request>
</AutoCreate>
"""

headers = {'Content-Type': 'application/xml',

		   'Content-transfer-enconding' : 'text'}

print requests.post(url, verify=False, data=xml, headers=headers).text

