import sys
import urllib
import httplib
import json

# setup
uri = '127.0.0.1'
headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
arg1 = sys.argv[1]

# connect & request
conn = httplib.HTTPConnection(uri, 5000)
conn.request("GET", "/test/" + str(arg1), '', headers)

# response & read
response = conn.getresponse()
data = response.read()

# close
conn.close()

# parse json
json_result = json.loads(data)

print json_result
