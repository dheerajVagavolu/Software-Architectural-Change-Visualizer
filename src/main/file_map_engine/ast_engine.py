# For testing
import os
import re
# from ast_helper import wrapper_get

# test_path = 'D:\Code\AC2\AC2\src\main\\test\Python\\game_of_life\game_o_life.py'
# # # test_path = os.path.abspath(test_path)
# code = open(test_path, 'r').read()

import ast
import json

def classname(cls):
    return cls.__class__.__name__

def jsonify_ast(node, level=0):
    fields = {}
    try:
        for k in node._fields:
            fields[k] = '...'
            v = getattr(node, k)
            if isinstance(v, ast.AST):
                if v._fields:
                    fields[k] = jsonify_ast(v)
                else:
                    fields[k] = classname(v)

            elif isinstance(v, list):
                fields[k] = []
                for e in v:
                    fields[k].append(jsonify_ast(e))

            elif isinstance(v, str):
                fields[k] = v

            elif isinstance(v, int) or isinstance(v, float):
                fields[k] = v

            elif v is None:
                fields[k] = None

            else:
                fields[k] = 'unrecognized'

        ret = { classname(node): fields }
        return ret
    except:
        ret = { classname(node): fields }

def make_ast(code):

    new_code = re.sub(r'print .*(\\\n.*)+', 'print("pass")\n',  code)
    
    new_code = re.sub(r'print .*\n', 'print("pass")\n',  new_code)
 
    new_code = re.sub(r'except.*:', 'except:',  new_code)
 
    new_code = re.sub(r'0700', '\'0700\'',  new_code)

    new_code = re.sub(r'%\(.*\)s', 'continue',  new_code)

    new_code = re.sub(r'% var', '',  new_code)

    # new_code = re.sub(r'""")', ')"""',  new_code)

    # new_code = re.sub(r'Debugging routines.', '# Debugging routines.',  new_code)


    new_code = re.sub(r'def print("pass")', 'def print("pass"):',  new_code)

    tree = ast.parse(new_code)
    return jsonify_ast(tree)

# new_tree = make_ast(code)
# final_obj = wrapper_get(new_tree, 'test')
# print(final_obj)
