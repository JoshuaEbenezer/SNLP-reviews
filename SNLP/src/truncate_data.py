import numpy as np
import sys

with open('/home/josh/python/SNLP/src/truncate_data/zero_filter/word_filter.json') as fileobj:
	head = [next(fileobj) for x in range(10000)]
with open('test.json',"w+") as writefile:
	for item in head:
		writefile.write(item)
