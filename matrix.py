from random import randrange as rr

m1 = [[1, 2, 3],    # -> [' 1', ' 2', ' 3'] -> ' 1 2 3' -> '1 2 3'
      [4, 5, 6],    # ...
      [7, 8, 9]]    # ['1 2 3', '4 5 6', '7 8 9'] -> '1 2 3\n4 5 6\n7 8 9'

m2 = [[rr(-15, 15) for _ in range(3)] for _ in range(3)]


def printmatrix(matrix: list[list[int]]) -> None:
    mx_wd = max(len(str(num)) for row in matrix for num in row) + 1
    print('\n'.join(''.join(f"{val:>{mx_wd}}" for val in row).strip() for row in matrix))

def printmatrix(matrix: list[list[int]]) -> None:
    val_lens = ()
    for row in matrix:
        for num in row:
            val_lens += (len(str(num)),)
    mx_wd = max(val_lens) + 1
    rows = ()
    for row in matrix:
        row_str = ''
        for num in row:
            row_str += str(num).rjust(mx_wd)  # эквивалентно f"{num:>{mx_wd}}"
        rows += (row_str[1:],)
    print(*rows, sep='\n')

def printmatrices(matrix1: list[list[int]], /, *matrices) -> None:
    matrices = (matrix1,) + matrices
    for matrix in matrices:
        printmatrix(matrix)
        print()

def printmatrices_line(matrix1: list[list[int]], /, *matrices) -> None:
    matrices = (matrix1,) + matrices
    for matrix in matrices:
        printmatrix(matrix)
        print()


printmatrix(m1)
print()
printmatrix(m2)
print()

printmatrices(m1, m2)
