import random as rd

# первое (берем длину множества сгенерированого списка)
print(len(set(rd.randint(1, 20) for i in range(0, 20))))

# второе (тоже самое только от обьединенных множеств)
print(len(
    set(rd.randint(1, 10) for j in range(0, 10)) |
    set(rd.randint(5, 15) for k in range(0, 10)))
)
