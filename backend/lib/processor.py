import os
import json
import numpy as np

class Processor:
    filepath = '/data/'
    def __init__(self):
        files = []

        for file in os.listdir(filepath):
            files.append(os.path.splitext(file)[0])

        number_of_docs = len(files);
        docs_per_block = number_of_docs / float(np.log(number_of_docs))

        z = 0

        for i in range (0, number_of_docs, int(docs_per_block)):
            if i + docs_per_block < number_of_docs:
                size = docs_per_block

            else:
                size = number_of_docs - i - 1;

            
            block = Block (i)
            
            for j in range (0, int(size)):
                block.insert_doc(files[z])
                # here the inverted index in doc
                z += 1

            block.write_block (number_of_docs)



class Block:
    block_id = 0;
    docs = {}
    words = {}
    
    def __init__ (self, id: int):
        self.block_id = id

    
    def insert_doc(self, file: str):
        self.docs[file] = 0


    def add_count(self):
        self.docs += 1


    def write_block(self, number_of_docs: int):
        data = {}
        
        data["docs"] = self.docs
        data["words"] = self.words
    
    
        with open (str(self.block_id) + '.json', 'w') as file:
            json.dump(data, file, ensure_ascii=False)

    
    def read_block(self, block_id: int):
        with open(str(block_id) + '.json') as file:
            data = json.load(file)

            self.doc = data["docs"]
            self.words = data["words]

