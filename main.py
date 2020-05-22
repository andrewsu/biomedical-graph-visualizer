import os
from flask import Flask, render_template, request, Response, jsonify
from module.queries.graph_utils import subgraph_tool
from module.queries.constants import *
import json

app = Flask(__name__)

# define routing
@app.route('/')
@app.route('/home')
def main():
    return render_template("home.html")

@app.route('/tool1')
def tool1():
    return render_template("tool1.html")

@app.route('/tool2')
def tool2():
    return render_template("tool2.html")

@app.route('/tool1/search', methods=['GET', 'POST'])
def graph_search():
    starting_node = request.form.get('starting_node', default = None, type = str)
    ending_node = request.form.get('ending_node', default = None, type = str)
    hops = request.form.get('hops', default = 3, type = int)

    '''example = {
        "results": [
            {"name": "Metformin", "domain": "Drug", "path_length": 1},
            {"name": "BRCA1", "domain": "Gene", "path_length": 3},
        ],
        "graph": {
             "nodes": [
               { "qid": "Q227339", "label": "BRCA1", "domain": "Gene"},
               { "qid": "Q17487737"   , "label": "BRCA1 DNA repair associated", "domain": "Protein" },
               { "qid": "Q19484", "label": "Metformin", "domain": "Drug" }
             ],
             "links": [
               { "target": "Q227339", "source": "Q17487737" , "weight": 0.01, "label": "encoded by" },
               { "target": "Q227339", "source": "Q19484" , "weight": 0.01, "label": "Made up Edge" },
               { "target": "Q17487737", "source": "Q19484" , "weight": 0.01, "label": "Made up Edge 2" }
             ]
           }
    }'''

    print(starting_node, ending_node, hops)

    results = subgraph_tool(starting_node, ending_node, hops, max_results=1000)

    return jsonify(results)

@app.route('/tool2/search', methods=['GET', 'POST'])
def similarity_search():
    data = request.get_json()
    targets = []
    if "targets" in data:
        targets = data["targets"]

    example = [
        {"label": "Metformin", "id": "Q19484", "sim_score": 1.5 , "pc1": 100, "pc2": 100},
        {"label": "BRCA1", "id": "Q227339", "sim_score": 3 , "pc1": 250, "pc2": 105},
        {"label": "BRCA1 DNA repair associated", "id": "Q17487737", "sim_score": 10 , "pc1": 40, "pc2": 182},
    ]
    return jsonify(example)

if __name__=='__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)