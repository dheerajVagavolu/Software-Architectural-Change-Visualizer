import os
import sys
import re

def parse(test_path):
    print("File detected: ", test_path)
    _file = open(test_path).readlines()
    print(len(_file))

    prev_indent = -1
    cur_indent = 0
    
    parent_dict = {}
    parent = {}


    parent_calls = {}

    parent[-1] = 'this_file'
    
    for sent in _file:
        tokens = sent.strip().split(' ')
        # Only consider lines which have actual content
        sent_str = sent.strip()
        if len(sent_str) > 0:
            indent = len(sent) - len(sent.lstrip())
            indent_lev = get_indent_level(indent)

            # print(get_indent_level(indent))
            
            #Chech if the line is a function definition
            cur_indent = indent_lev

            status = 0
            
            if prev_indent - cur_indent == 0:
                # print('same level')
                status = 0
            elif prev_indent - cur_indent < 0:
                print('increase in level')
                status = 1
            else:
                print('decrease in level')
                status = -1

            prev_indent = cur_indent

            func_name = re.search("[a-zA-Z]+[a-zA-Z0-9_]*\(", sent_str)
            

            if func_name:
                act_func = func_name.group()[:-1]

                # Is a function defintion
                if tokens[0] == 'def':
                    func_name = re.search("[a-zA-Z]+[a-zA-Z0-9_]*\(", sent_str)
                    print("function definition: ", func_name.group()[:-1])
                    
                    
                    if parent[indent_lev-1] not in parent_dict.keys():
                        parent_dict[parent[indent_lev-1]] = [act_func]
                    else:
                        parent_dict[parent[indent_lev-1]].append(act_func)
                    # parent_dict[act_func] = parent[indent_lev-1]
                    parent[indent_lev] = act_func
                    
                
                else:
                    print(indent_lev, ' function name: ', func_name.group()[:-1])

                    if parent[indent_lev-1] not in parent_calls.keys():
                        parent_calls[parent[indent_lev-1]] = [act_func]
                    else:
                        parent_calls[parent[indent_lev-1]].append(act_func)

            else: # Is a Condition
                tok = ['if', 'elif', 'else:', 'for', 'while','switch']
                if tokens[0] in tok:
                    act_func = tokens[0]+'_'+str(parent[indent_lev-1])

                    print("Condition: ", act_func)
                    if parent[indent_lev-1] not in parent_dict.keys():
                        parent_dict[parent[indent_lev-1]] = [act_func]
                    else:
                        parent_dict[parent[indent_lev-1]].append(act_func)
                    # parent_dict[act_func] = parent[indent_lev-1]
                    parent[indent_lev] = act_func

            if sent_str.find('__main__')!=-1:
                print('function name: ', 'main')


    print(parent_dict)
    print(parent_calls)

    return 0

def get_indent_level(cur):
    return int(cur/4)


