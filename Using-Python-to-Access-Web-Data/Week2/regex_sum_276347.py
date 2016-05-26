#!/usr/bin/env python
import re
def calcu(file):
	nums = []
	sum = 0
	with open(file) as f:
		for line in f.readlines():
			for ele in re.findall('[0-9]+',line):
				nums.append(ele)
	for dig in nums:
		sum += int(dig)
	return sum
if __name__ == '__main__':
	sum = calcu("regex_sum_276347.txt")
	print(sum)
