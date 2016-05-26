#!/usr/bin/env python3
import urllib.request
from bs4 import BeautifulSoup

url = input('Enter - ')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html,'lxml')

tags = soup('a')
for num_time in range(6):
	print(tags[17].get("href"))
	url = tags[17].get('href')
	html = urllib.request.urlopen(url).read()
	soup = BeautifulSoup(html, 'lxml')
	tags = soup('a')
print(tags[17].get_text())
