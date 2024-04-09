import urllib.request, urllib.error, urllib.parse
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors#
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url ="https://py4e-data.dr-chuck.net/comments_2002806.html"
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the number and sum in total#

total = 0
tag = soup('span')

for i in tag:
    total += int(i.text)
print(total)
