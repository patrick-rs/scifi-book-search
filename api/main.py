from flask import Flask, send_from_directory, request
from elasticsearch import Elasticsearch
import os
from flask_cors import CORS



app = Flask(__name__)
CORS(app)

es = Elasticsearch(
        os.environ["ELASTIC_URL"],
        verify_certs=False,
        basic_auth=("elastic", os.environ["ELASTIC_PASSWORD"])
        )

@app.route("/api/search")
def search_books():
    query = request.args.get("query")
    resp = es.search(index="scifi_books", query={    "multi_match": {
        "query":     query,
        "fields":  ["Author_Name", "Book_Description", "Book_Title", "Book_Type"],
        "fuzziness": "AUTO",
        "operator":  "and"
    }
})
    return resp.body["hits"]["hits"]


@app.route("/")
def serve_website():
    return send_from_directory("dist", path="index.html")

@app.route("/vite.svg")
def serve_website_svg():
    return send_from_directory("dist", path="vite.svg")