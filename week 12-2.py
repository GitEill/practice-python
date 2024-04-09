import urllib.request, urllib.error, urllib.parse
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors#
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url ="http://py4e-data.dr-chuck.net/known_by_Gabby.html"
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Find the 18th anchor tag, find the name that associates with #
#go into the link and repeat the search 7 times#
Tag = soup('a')
print(Tag)
count = 0
while count < 7:
    new_url = Tag[17]['href']
    print(Tag[17].get_text())
    count += 1
    html = urlopen(new_url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    Tag = soup('a')


