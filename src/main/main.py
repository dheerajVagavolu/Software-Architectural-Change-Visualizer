# from ..file_map_engine.engine import parse
import os
import ast
from os import path
from pprint import pprint
import json
import ast
from flask import Flask, render_template, redirect, request, url_for
import sys
from file_map_engine.engine import get_calls
from file_map_engine.call_dir import dir_walk
from file_map_engine.ast_engine import make_ast
from file_map_engine.ast_helper import wrapper_get
import pickle

cur_dir = os.getcwd()
# from test import make_ast

app = Flask(__name__)

# @app.route('/')
# def new_page():
#     return render_template('home.html')

# @app.route('/download_data', methods=['POST'])
# def download():
#     github = request.form['github']
#     print(github)

#     cmd = "git clone "+github
#     cmd2 = 'git tag --sort=committerdate > ../tags.txt'


#     test_dir = cur_dir+'/test'
#     os.chdir(test_dir)
#     os.system(cmd)

#     cur = os.getcwd()
#     repo_dir = cur + '\\' + github.split('/')[-1].split('.')[0]
#     os.chdir(repo_dir)
#     os.system(cmd2)
#     os.chdir(test_dir)

#     tags = open('tags.txt').readlines()

#     os.chdir(repo_dir)
    
#     ulti_dict = {}
#     ulti_tree = {}
    
#     num = 0

#     for i in tags:
#         num += 1
#         print("\n\n\n New Tag: ", i, "\n\n")

        
#         cmd3 = 'git checkout ' + i
#         os.system(cmd3)
        

#         os.chdir(cur_dir)


#         new_dir = os.path.join(os.getcwd(), 'test')
#         tree = dir_walk(new_dir)


#         #https://github.com/kupferlauncher/kupfer.git
#         returned_tree = get_dictionary(tree)

#         ulti_tree[str(num)] = tree
#         ulti_dict[str(num)] = returned_tree
        
#         os.chdir(repo_dir)
    
        
    
#     os.chdir(cur_dir)
#     pickle.dump( ulti_dict, open( "ulti_dict2.dat", "wb" ))
#     pickle.dump( ulti_tree, open( "ulti_tree2.dat", "wb" ))
    
#     return redirect('/run')

@app.route('/')
def hello_world():
    
    script_dir = os.getcwd()

    # test_path = 'test/file.py'

    # test_path = 'test'

    new_dir = os.path.join(os.getcwd(), 'test')
    tree = dir_walk(new_dir)
    # new_calls_tree = get_dictionary(tree)
    
    # print(tree)


    # This if for engine of parsing.

    ########################################################################################
    new_calls_tree = pickle.load( open( "test2.dat", "rb" ) )
    ulti_dict = pickle.load( open( "ulti_dict2.dat", "rb" ) )
    new_ulti_dict = json.dumps(ulti_dict)
    # print(new_ulti_dict['1']['D:\\Code\\AC2\\AC2\\src\\main\\test\\class.py'])
    ulti_tree = pickle.load( open( "ulti_tree2.dat", "rb" ) )
    print(new_ulti_dict)
    tags = open('test/tags.txt').readlines()

    # print(ulti_dict['51'])
    # print(ulti_dict['6'])
    # print(ulti_dict['7'])
    # print(ulti_dict['8'])
    


    # temp_tree ,temp_mod = get_calls(i['value'])
    # print(temp_mod)
    
    ########################################################################################
            


    return render_template('index.html', tags = tags, ulti_tree = {'body': ulti_tree} ,ulti_dict = new_ulti_dict, tree = tree, calls = new_calls_tree)
    # return "hello_world"

def get_dictionary(tree):

    new_calls_tree = {}

    for k in tree.keys():
        print(k, "\n-------------")
        for i in tree[k]:
            if i['type'] == 'file':
                if i['value'].split('.')[-1] == 'py':
                    # print(i['value'])
                    code = open(i['value'], 'r', encoding='utf-8').read()
                    new_tree = make_ast(code)
                    final_obj = wrapper_get(new_tree, i['value'])
                    # print(final_obj)
                    print("successful")
                    if i['value'] not in new_calls_tree.keys():
                        new_calls_tree[i['value']] = dict(final_obj)
    
    # pickle.dump( new_calls_tree, open( "test2.dat", "wb" ))

    return new_calls_tree

if __name__ == '__main__':

    app.run(debug = True)

    
# call_list, imp_dict = get_calls(test_path)
# print(call_list)
# print(imp_dict)


    
