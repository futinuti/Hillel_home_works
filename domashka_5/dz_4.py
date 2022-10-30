n = int(input())
print(n, end='  ')
for i in range(1, n+1):
    if i ** 2 <= n:
        print(i ** 2, end=' ')
