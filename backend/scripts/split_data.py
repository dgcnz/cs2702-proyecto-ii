import pandas as pd
import json
from tqdm import tqdm

FILES = ["articles1.csv"]

for FILE in tqdm(FILES):
    df = pd.read_csv(FILE)
    for _, row in tqdm(df.iterrows(), total=len(df)):
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
