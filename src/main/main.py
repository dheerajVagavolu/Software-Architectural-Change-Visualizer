# from ..file_map_engine.engine import parse
import os
from os import path

if __name__ == "__main__" :
    import sys
    script_dir = os.getcwd()
    sys.path.append(path.join(path.dirname(__file__), '..'))
    from file_map_engine.engine import parse
    
    test_path = 'test/file.py'
    # abs_file_path = os.path.join(script_dir, test_path)
    
    parse(test_path)
    
