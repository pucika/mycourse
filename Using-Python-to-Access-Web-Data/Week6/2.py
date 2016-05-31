#!/usr/bin/env python3
import urllib.request
import urllib.parse
import json

serviceurl = "http://python-data.dr-chuck.net/geojson?"

while True:
	address = input(r'Enter location: ')
	if len(address) < 1 : break

	url = serviceurl + urllib.parse.urlencode({'sensor':'false', 'address':address})
	print('Retrieving', url)
	uh = urllib.request.urlopen(url)
	data = uh.read()
	print('Retrieved',len(data), 'characters')

	try: 
		js = json.loads(data.decode())
	except: js = None
	if 'status' not in js or js['status'] != 'OK':
		print('====Failure To Retrieve ====')
		print(data)
		continue
	print(js['results'][0]['place_id'])
