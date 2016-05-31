#!/usr/bin/env python3
import urllib.request
import xml.etree.ElementTree as ET

serviceurl = 'http://python-data.dr-chuck.net/comments_276349.xml'
sum = 0
html =  urllib.request.urlopen(serviceurl).read()
tree = ET.fromstring(html)
for num in tree.findall('.//count'):
	print(num)
print("Sum: ",sum)