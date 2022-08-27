from pathlib import Path
from sys import argv

# навигация вверх (к корню файловой системы)
SCRIPT_DIR = Path(argv[0]).parent
# навигация вниз
textfile = SCRIPT_DIR / 'text_file.txt'

# перебор объектов в каталоге
for path in SCRIPT_DIR.iterdir():
    if path.is_file():
        prefix = '- '
    elif path.is_dir():
        prefix = 'd '
    else:
        prefix = '  '
    # print(prefix + path.name)

# поиск объектов по шаблону
for path in SCRIPT_DIR.glob('*.txt'):
    print(path.name)
print('\n')

for path in SCRIPT_DIR.glob('*func*.*'):
    print(path.name)
print('\n')

