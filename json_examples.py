from pathlib import Path
from sys import path

from json import load, loads, dump, dumps

from pprint import pprint


source_file = Path(path[0]) / 'j_test.json'
target_file = Path(path[0]) / 'j_test_out.json'

# трансляция из JSON файла в Python объект
with open(source_file, encoding='utf-8') as filein:
    data = load(filein)
print(type(data))

# трансляция из Python объекта в JSON строку
data_str = dumps(data, ensure_ascii=False, indent=2)
print(type(data_str))

# трансляция из JSON строки в Python объект
data = loads(data_str)
print(type(data))

data['stay cost'] = 1.5

# трансляция из Python объекта в JSON файл
with open(target_file, 'w', encoding='utf-8') as fileout:
    dump(data, fileout, ensure_ascii=False, indent=2)
