import pandas as pd
import numpy as np
import json
df = pd.read_csv('/home/josh/python/SNLP/src/truncate_data/zero_filter/filtered.csv')
j = len(df.index)
df = df[df.word_count < 500]
df = df[df.word_count >10]

out = df.to_json(orient='records')[1:-1].replace('},{', '}\n{')
with open('word_filter.json', 'w') as f:
    f.write(out)
