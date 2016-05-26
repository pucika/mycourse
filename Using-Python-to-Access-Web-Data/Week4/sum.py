#!/usr/bin/env python3
import urllib.request
import re
from bs4 import BeautifulSoup

url = input('Enter - ')
html = urllib.request.urlopen(url).read()

soup = BeautifulSoup(html, "lxml")
sum = 0
for num in soup.findAll('span'):
	sum += int(num.get_text())
print(sum)
