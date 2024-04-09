import urllib.request, urllib.parse, urllib.error
import ssl
import json

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#Api endpoint server url#
serviceurl = 'http://py4e-data.dr-chuck.net/opengeo?'

# Look for the input location#
while True:
    loc = input('Enter a location:')
    if len(loc) < 1:
        break

#Get the json date of the desired location from the server#
    print('The plus code you want to know is:', loc)
    loc = loc.strip()
    xpath =dict()
    xpath['q'] = loc
    url = serviceurl + urllib.parse.urlencode(xpath)
    print('Retrieving:', url)

#Retrive the location json from the server and display#
    handle = urllib.request.urlopen(url, context = ctx)
    pre_data = handle.read().decode()
    print('total of',len(pre_data), 'characters')
    
    try: 
        Data = json.loads(pre_data)
    except:
        Data = None
        print('Invalid location')

    if not Data or 'features' not in Data:
        print('Failed to retrieve location')
        print(pre_data)
        break
    if len(Data['features']) == 0:
        print('No record exist')
        print(pre_data)
        break

#Parse the json data, retrieve the first plus code#

    pluscode = Data['features'][0]['properties']['plus_code']
    print('Found Plus code:', pluscode)
