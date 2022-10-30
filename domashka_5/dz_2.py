number_to_check = int(input('Write natural number N:'))
cnt = 0
dlina = number_to_check
while dlina > 0:
    cnt += 1
    dlina //= 10
for i in range(1, number_to_check+1):
    for stage in range(1, cnt+1):
        if i == i*i % 10**stage:
            print(i, '*', i, '=', i*i)
            break
