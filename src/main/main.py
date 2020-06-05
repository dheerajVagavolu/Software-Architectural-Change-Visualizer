# from ..file_map_engine.engine import parse
import os
import ast
from os import path
from pprint import pprint
import json
import ast
from flask import Flask, render_template
import sys
from file_map_engine.engine import get_calls
from file_map_engine.call_dir import dir_walk
import networkx as nx
import matplotlib.pyplot as plt

app = Flask(__name__)

@app.route('/')
def hello_world():
    script_dir = os.getcwd()
    test_path = 'test/file.py'
    test_path = 'test'
    new_dir = os.getcwd() + '\\test'
    tree = dir_walk(new_dir)
    print(tree)

    # G=nx.Graph()

    # # adding just one node:
    # # a list of nodes:
    # G.add_nodes_from(tree.keys())

    # for key in tree.keys():
    #     for te in tree[key]:
    #         if te['type'] == 'dir':
    #             G.add_edge(key, te['value'])
    #         elif te['type'] == 'file':
    #             G.add_node(te['value'])
    #             G.add_edge(key, te['value'])

    # print("Nodes of graph: ")
    # print(G.nodes())
    # print("Edges of graph: ")
    # print(G.edges())

    # nx.draw(G)
    # plt.savefig("test.pdf")

    return render_template('index.html', tree = tree)

if __name__ == '__main__':



    app.run(debug = True)

    
# call_list, imp_dict = get_calls(test_path)
# print(call_list)
# print(imp_dict)


    
