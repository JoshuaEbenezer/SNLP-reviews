import pandas as pd
import numpy as np
import json
df = pd.read_csv('/home/josh/python/SNLP/src/truncate_data/zero_filter/zero_filter.csv')
df['word_count'] = pd.Series(0, index=df.index)
j = len(df.index)
with open('filtered_count.txt', 'w+') as f:
	for x in range(0, j):
		count = len(df.iloc[x,8].split())
		df.iloc[x,11] = count
		#print (df.iloc[x,10])
		f.write('{}\n'.format(count))
out = df.to_json(orient='records')[1:-1].replace('},{', '}\n{')
with open('filtered.json', 'w+') as fout:
    fout.write(out)


    	
