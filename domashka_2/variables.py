# Вариант 1
first_box = 12
second_box = 75

print("Вариант 1\n", first_box, second_box)

buffer_box = first_box
first_box = second_box
second_box = buffer_box

print(first_box, second_box)

# Вариант 2
first_box = 15
second_box = 33

print("Вариант 2\n", first_box, second_box)

first_box, second_box = second_box, first_box

print(first_box, second_box)

# Вариант 3
first_box = 15
second_box = 99

print("Вариант 3\n", first_box, second_box)

first_box = first_box + second_box
second_box = first_box - second_box
first_box = first_box - second_box

print(first_box, second_box)