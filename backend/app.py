from flask import Flask, render_template, request, redirect, url_for, Response, flash
import json
import importlib
import sys
import os 
import glob
#from index import Query
#import index
import time
from lib.iixdisk import DiskInvertedIndex
from pathlib import Path

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

app = Flask(__name__,
            static_url_path='', 
            static_folder='../frontend/static',
            template_folder='../frontend/templates')

@app.route('/')
def home():
   return render_template('search-engine.html')

def serializeNew(fileName):
    f = open(fileName, "r")
    parse_file = json.loads(f.read())
    return {
        "id": parse_file["id"],
        "title": parse_file["title"][0:150],
        "content": parse_file["content"][0:300],
        "author": parse_file["author"],
        "date": parse_file["date"]
    }

def serializeFullNew(fileName):
    f = open(fileName, "r")
    parse_file = json.loads(f.read())
    return {
        "id": parse_file["id"],
        "title": parse_file["title"],
        "content": parse_file["content"],
        "author": parse_file["author"],
        "date": parse_file["date"]
    }


def serializeQueryResponse(queryResponse):
    response = []
    for t in queryResponse:
        response.append(serializeNew(t[0]))
    return response


@app.route('/get-new-by-id', methods = ['POST'])
def get_by_id():
    request_body = json.loads(request.data)
    id = str(request_body['id'])

    response = Response(
         response= json.dumps(serializeFullNew('data/'+id+'.json')),
         status=200,
         mimetype='application/json'
    )
    return response

@app.route('/get-news', methods = ['POST'])
def consulta():
    request_body = json.loads(request.data)
    search_words = request_body['words']
    k_value = request_body['k_value']
    if(k_value.isnumeric()):
        k = int(k_value)
    else:
        k = 10
    iix = DiskInvertedIndex(Path('data'), True)
    query_response = iix.query(search_words, k)
    print(k_value)

    response = Response(
         response= json.dumps(serializeQueryResponse(query_response)),
         status=200,
         mimetype='application/json'
    )
    return response

if __name__ == '__main__':
   app.run()