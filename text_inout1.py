# чтение
#   способ 1
f_in = open(r"text_file.txt", 'r', encoding='utf-8')
text = f_in.read()
f_in.close()

print(text, end='\n'*3)

#   способ 2
with open(r"text_file.txt", 'r', encoding='utf-8') as f_in:
    lines = f_in.readlines()

print(lines, end='\n'*2)


# запись
#   перезапись
text_to_write = ''.join(lines).upper()
with open(r"text_file.txt", 'w', encoding='utf-8') as f_out:
    f_out.write(text_to_write)

#   дозапись
lines_to_write = reversed(lines + ['\n'])
with open(r"text_file.txt", 'a', encoding='utf-8') as f_out:
    f_out.writelines(lines_to_write)
