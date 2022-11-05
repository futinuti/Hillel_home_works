row = int(input("Input Number : "))
for i in range(row):
    print(f'{i: >5} {"1" + "0" * i: >{row}}')
