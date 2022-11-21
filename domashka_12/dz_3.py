from random import randint


def gen_prime_numbers(n, z):
    """
    :param n: start
    :param z: finish
    :return: nothing
    """
    # print('n', n, 'z', z)
    if n > z:
        n, z = z, n
    count = 0
    for char in range(n, z + 1):
        tag = 1
        for i in range(2, int(char)):
            if char % i != 0:
                tag = 0
            if char % i == 0:
                tag = 1
                break
        if tag == 0 or char == 2:
            print(char, end=' ')
            count += 1
    if count == 0:
        print("Empty")
    print("\n")


gen_prime_numbers(100, 0)
gen_prime_numbers(510, 520)  # Empty
gen_prime_numbers(randint(500, 1000), randint(500, 1000))
