from pathlib import Path
from sys import argv
from pprint import pprint

# навигация вверх (к корню файловой системы)
SCRIPT_DIR = Path(argv[0]).parent
# навигация вниз
textfile = SCRIPT_DIR / 'text_file.txt'

# lines = []
# with open(textfile, encoding='utf-8') as f_in:
    # for line in list(f_in):
        # line_cl = line.strip()
        # if line_cl:
            # lines.append(line_cl)

text = textfile.read_text(encoding='utf-8')
lines = [
    line_cl
    for line in text.split('\n')
    if (line_cl := line.strip())
]

pprint(lines)
