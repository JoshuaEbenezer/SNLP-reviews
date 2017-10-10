'''
Convert Yelp Academic Dataset from JSON to CSV
Requires Pandas (https://pypi.python.org/pypi/pandas)
By Paul Butler, No Rights Reserved
'''

import json
import pandas as pd
from glob import glob

def convert(x):
    ''' Convert a json string to a flat python dictionary
    which can be passed into Pandas. '''
    ob = json.loads(x)
    for k, v in ob.items():
        if isinstance(v, list):
            ob[k] = ','.join(v)
        elif isinstance(v, dict):
            for kk, vv in v.items():
                ob['%s_%s' % (k, kk)] = vv
            del ob[k]
    return ob

json_filename = '/home/josh/python/SNLP/src/truncate_data/zero_filter/test.json'
f = open(json_filename)
csv_filename = '%s.csv' % json_filename[:-5]
df = pd.DataFrame([convert(line) for line in f])
df.to_csv(csv_filename, encoding='utf-8', index=False)