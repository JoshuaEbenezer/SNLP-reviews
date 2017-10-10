import numpy as np
import sys

with open('sorted_freq.txt', 'w+') as out:
	with open('useful_freq.txt') as file:
		for line in sorted(file, key=lambda line: line.split()[0]):
			out.write(line)


	
