import numpy as np
import sys
import re

with open('./word/token_freq.txt') as fileobj:
	with open('token_frq.txt', 'w+') as output_file:
		for line in fileobj:
			line = line.replace(' ', '\t')
			output_file.write(line)
        	

        	
        	



