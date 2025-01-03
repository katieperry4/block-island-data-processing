import json
import gzip

with open('elevation_data1.json', 'r') as file:
    data = json.load(file)

with gzip.open("compressed_data1.gz", "wt", encoding='utf-8') as f:
    json.dump(data, f)