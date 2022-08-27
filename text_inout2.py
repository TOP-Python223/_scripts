with open('bool.py') as f_in:
    codelines = f_in.readlines()

for i in range(len(codelines)):
    if 'complex' in codelines[i]:
        print(f"'complex' > {i+1}: {codelines[i].strip()}")
