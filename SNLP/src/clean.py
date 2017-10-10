import re
from unidecode import unidecode
F = open('review.json', 'r')

out = re.sub(r'([^"0-9]),[^"]', r'\1 ', F.read())
out = re.sub(r'[^\x00-\x7F]+', r'', out);
with open('cleaned_rev.json', 'w') as f:
f.write(out)