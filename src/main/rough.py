from file_map_engine.ast_engine import make_ast


test_path = 'test\python\examples\\custom_object.py'
code = open(test_path, 'r').read()

tree = make_ast(code)

print(tree.keys())