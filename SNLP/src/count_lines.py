import sys

linecount = 0
with open('english_rev.json') as fileobj:
	for line in fileobj:
		linecount = linecount + 1
print (linecount)
