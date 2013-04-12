import sys
import urllib
import httplib
import json

# setup
uri = '127.0.0.1'
headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
arg1 = sys.argv[1]
arg2 = sys.argv[2]
params = urllib.urlencode({'key': arg1, 'name': arg2})

# connect & request
conn = httplib.HTTPConnection(uri, 5000)
conn.request("POST", "/test/new", params, headers)

# response & read
response = conn.getresponse()
#data = response.read()

# close
conn.close()