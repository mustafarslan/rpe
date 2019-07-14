from flask import Blueprint, request
from elasticsearch import Elasticsearch
client_blueprint = Blueprint('client', __name__)
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])


@client_blueprint.route("/clienttest")
def test():
    return "Client test!"


@client_blueprint.route("/averageprices")
def client_get_request():
    date = request.args.get('date')
    website = request.args.get('website')
    res = es.search(index="sample_database", body={"query": {"bool": {"must": [{ "match": {"datePublishedObject.value": date}},{ "match": {"isBasedOnUrlObject.id": website} }]}}})
    return {"msg": res['hits']['hits']}


@client_blueprint.route("/getwebsites")
def get_all_websites():
    date = request.args.get('date')
    res = es.search(index="sample_database", body={"query": {"bool": {
        "must": [{"match": {"datePublishedObject.value": date}}]}}})
    return {"msg": res['hits']['hits']}