import urllib, urllib2

from urllib2 import urlopen

data = open("config.xml", 'r')

header = """
Content-Type:text/xml
Content-transfer-encoding: text
"""

url= "https://41.220.12.206/services/yopaymentsdev/task.php"

req = urllib2.Request(url)
req.add_header("Content-Type", "text/xml")
req.add_header("Content-transfer-encoding", "text")
req.add_data(data.read())

data.close()

response = urlopen(req)

print response
