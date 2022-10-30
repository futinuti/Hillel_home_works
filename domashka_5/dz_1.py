number_to_check = input()
cnt = 0
for i in number_to_check:
    if cnt == 2:
        break
    cnt = 0
    for j in number_to_check:
        if j == i:
            cnt += 1
print('\033[1mТак\033[0m' if cnt == 2 else '\033[1mНі\033[0m')
