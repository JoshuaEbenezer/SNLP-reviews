from collections import Counter
import csv

with open('filtered_count.txt') as f:
    wordcount = Counter(f.read().split())
with open('filter_freq.txt','w+') as fout:
	for k,v in wordcount.items():
		print(k, '\t', v, file = fout)
        