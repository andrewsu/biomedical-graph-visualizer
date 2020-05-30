import os
import json

from downloader import query
from queries.constants import *
from queries.graph_utils import *
import argparse

def download_all_data():
    print("Downloading from Wikidata....")
    if not os.path.exists(DOWNLOAD_DIR):
        os.mkdir(DOWNLOAD_DIR)
    for (concept1, concept2) in EDGES_DICT:
        mapping = EDGES_DICT[(concept1, concept2)]
        if type(mapping) is not list:
            mapping = [mapping]
        for relation, query_template in mapping:
            concept1_id, concept2_id = CONCEPT_LABEL_ID_DICT[concept1], CONCEPT_LABEL_ID_DICT[concept2]
            relation_id = RELATION_LABEL_ID_DICT[relation]
            q = query_template(concept1_id, relation_id)
            print(q)
            res = query(q)

            with open(os.path.join(DOWNLOAD_DIR, "{}_{}_{}.tsv".format(concept1_id, concept2_id, relation_id)), "w", encoding="utf-8") as f:
                for entry in res["results"]["bindings"]:
                    # entry['concept']['value'] returns http://www.wikidata.org/entity/Q17815615. Only want id Q17815615.
                    instance1_id = entry['concept']['value'].split("/")[-1]
                    instance1_label = entry['conceptLabel']['value']
                    instance2_id = entry['peripheralConcept']['value'].split("/")[-1]
                    instance2_label = entry['peripheralConceptLabel']['value']
                    f.write("{}\t{}\t{}\t{}\n".format(instance1_id, instance1_label, instance2_id, instance2_label))


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--download', action="store_true", help='whether or not to download the graph')
    parser.add_argument('--autocomplete', action="store_true", help='whether or not to generate autocomplete json')
    args = parser.parse_args()

    download = args.download
    autocomplete = args.autocomplete

    if download:
        download_all_data()

    g = get_graph(replace_pickle=True)  # builds a new graph from local files and saves pickle

    if autocomplete:
        if not os.path.exists("../static/autocomplete/"):
            os.mkdir("../static/autocomplete/")
        save_all_node_names_ids_json(g, out_path="../static/autocomplete/all_node_names_ids.json")
        save_all_concept_names_ids_json(out_path="../static/autocomplete/all_concept_names_ids.json")
