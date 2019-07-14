from flask import Blueprint
from pymongo import MongoClient
import pandas as pd
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk, parallel_bulk
from collections import deque
from tqdm import tqdm
import time

database_blueprint = Blueprint('database', __name__)

mongoClient = MongoClient('mongodb://localhost:27017/')
db = mongoClient["sample_database"]
col = db["sample_collection"]


@database_blueprint.route("/databasetest")
def test():
    return "Database Test!"


@database_blueprint.route("/createdb")
def createDB():
    dataframe = pd.read_json('resources/sample.json', lines=True)
    print(dataframe.size)
    print(dataframe.head(1).datePublishedObject)
    data = dataframe.to_dict(orient='records')
    col_list = db.list_collection_names()
    if "sample_collection" in col_list:
        print("Collection exists")
    else:
        col = db["sample_collection"]
    col.insert_many(data)
    return {"msg": "Created"}


@database_blueprint.route("/cleandb")
def cleanDB():
    col.drop()
    return {"msg": "Deleted"}


@database_blueprint.route("/synctoelastic")
def syncToElastic():
    es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
    # Pull from mongo and dump into ES using bulk API
    actions = []
    for data in tqdm(col.find(), total=col.count()):
        data.pop('_id')
        action = {
            "_index": "sample_database",
            "_type": "document",
            "_source": data
        }

        es.index(index='sample_database', doc_type='sample_collection', body=data)
        # Dump x number of objects at a time

        time.sleep(.01)

    return {"msg": "Sync completed."}