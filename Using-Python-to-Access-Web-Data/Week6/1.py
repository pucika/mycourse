#!/usr/bin/env python3
import urllib.request
import json

url = input(r"Enter:")
html = urllib.request.urlopen(url).read()
nums = json.loads(html.decode())

sum = 0
for item in nums["comments"]:
	sum += item["count"]
print(sum)