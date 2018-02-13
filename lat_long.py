import requests
import json

send_url = 'http://freegeoip.net/json'
r = requests.get(send_url)
j = json.loads(r.text)
lat = j['latitude']
lon = j['longitude']

print(j)

import geocoder

g = geocoder.ip('1.186.47.2')
g1 = geocoder.ip('me')
print(g.latlng)
print(g1.latlng)


from requests import get
loc = get('https://ipapi.co/103.16.68.218/json/')
print(loc.json())