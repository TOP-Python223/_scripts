print('\'\"', end='\n\n')

# raw string
print(r"c:\windows\system32")
print(r"d:\education\top", end='\n\n')

print("d:\\education\\top", end='\n\n')

print("/etc")
print("/home/genndalf/top_academy", end='\n\n')


from pathlib import Path, PurePosixPath

# path-like object
path_win_core = Path(r"c:\windows\system32")
print(f'\n{path_win_core = }\n{type(path_win_core) = }\n')

path_unix_core = PurePosixPath("/home/genndalf/top_academy")
print(f'\n{path_unix_core = }\n{type(path_unix_core) = }\n')


