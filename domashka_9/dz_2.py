import random

n = int(input("Input N :"))

random_matrix = [[random.randint(0, 10)
                 for row in range(n)]
                 for column in range(n)]

sum_diagonals = sum([random_matrix[i][i] for i in range(n)])
# второстепенная диагональ
# sum_diagonals_2 = sum([random_matrix[i][n-1-i] for i in range(n)])
sum_last_column = sum([random_matrix[i][n - 1] for i in range(n)])

for row in random_matrix:
    print("[", end=" ")
    for elem in row:
        print(f'{elem:^4}', end=" ")
    print("]")
print(f'Sum of diagonals \\ : {sum_diagonals}')
# print(f'Sum of diagonals / : {sum_diagonals_2:.3f}')
print(f'Sum of last columns: {sum_last_column}')
