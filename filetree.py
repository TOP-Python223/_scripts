from pathlib import Path
from sys import path

dir_path = Path(path[0]).parent

for tree_element in dir_path.iterdir():
    print(tree_element.name)
