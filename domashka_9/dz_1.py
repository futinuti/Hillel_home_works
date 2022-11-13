n = int(input("Input N "))
matrix_1 = [[row if column % 2 != 0 else column for row in range(-n, 0)] for column in range(1, n + 1)]

for row in matrix_1:
    print("[", end=" ")
    for column in row:
        print(f'{column:4}', end=" ")
    print(" ]")
