summa = 0
cnt = 0
sr_arifm = 0
n_max, n_min = 0, 0
parnie, not_parnie = 0, 0
while True:
    a = int(input())
    if a == 0:
        break
    else:
        cnt += 1
        summa += a
        sr_arifm = summa / cnt
        if cnt == 1:
            n_max, n_min = a, a
        elif a > n_max:
            n_max = a
        elif a < n_min:
            n_min = a
        if a % 2 == 0:
            parnie += 1
        else:
            not_parnie += 1
if cnt > 0:
    print('1. Сумма чисел =', summa, '\n',
          '2. Середнє аріфметичне усіх чисел =', sr_arifm, '\n',
          '3. Максимальне =', n_max, 'Мінімальне =', n_min, '\n',
          '4. Кількість парних =', parnie, 'кількість не парних =', not_parnie)
