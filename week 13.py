import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/comments_2002808.xml'
xml = urllib.request.urlopen(url, context=ctx).read()

#find the number of count in string that is under comment tag and count in total#

counter = 0
tree = ET.fromstring(xml)
for count in tree.findall('.//count'):
    counter += int(count.text.strip())

print(counter)