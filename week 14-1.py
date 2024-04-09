import urllib.request, urllib.parse, urllib.error
import ssl
import json

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url ='http://py4e-data.dr-chuck.net/comments_2002809.json'
Json = urllib.request.urlopen(url).read()

#pares json data, find the value from count under each element#
info = json.loads(Json)
count = 0
for i in info['comments']:
    count += int(i['count'])
print('Count:', len(info['comments']))
print('Sum:', count)
