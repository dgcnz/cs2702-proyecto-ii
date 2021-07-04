import pandas as pd
import json
import argparse
from tqdm import tqdm
from math import inf

parser = argparse.ArgumentParser(description='Split csv into single documents')

parser.add_argument('input', type=str, nargs='+', help='Input files.')
parser.add_argument('--maxn',
                    dest='n',
                    type=int,
                    default=inf,
                    help='Max number of rows considered.')
args = parser.parse_args()

FILES = args.input
n = args.n

for FILE in tqdm(FILES):
    df = pd.read_csv(FILE)
    for _, row in tqdm(df.iterrows(), total=len(df)):
        if n <= 0:
            break
        n -= 1
        id = row['id']
        rowjson = {
            'id': row['id'],
            'title': row['title'],
            'publication': row['publication'],
            'author': row['author'],
            'date': row['date'],
            'content': row['content']
        }
        with open('data/' + str(id) + '.json', 'w') as f:
            f.write(json.dumps(rowjson))
