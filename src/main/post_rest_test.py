######################################
# POST /test/new/
######################################
import urllib
import httplib
import json

# setup
uri = '127.0.0.1'
headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
params = urllib.urlencode({'key': 2, 'name': 'hello'})

# connect & request
conn = httplib.HTTPConnection(uri, 5000)
conn.request("POST", "/test/new", params, headers)

# response & read
response = conn.getresponse()
#data = response.read()

# close
conn.close()