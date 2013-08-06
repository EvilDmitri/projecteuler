# coding=utf-8


def get_triangle(n):
    number = 0
    for x in xrange(1, n + 1):
        number += x
    return number


# Функция нахождения количества делителей натурального числа
def counter(a):
    count = 1
    k = 0
    if a == 1 or a == 2:
        return a

    while a & 1 == 0:
        k += 1
        a >>= 1
    if a == 1:
        return k + 1
    else:
        count = k + 1

    i = 3
    while i * i <= a:
        k = 0
        while a % i == 0:
            k += 1
            a /= i
        count *= (k + 1)
        i += 2

    if a > 1:
        count <<= 1
    return count


for x in xrange(10000, 50000):
    a = get_triangle(x)
    b = counter(a)
    print b
    if b > 500:
        print 'BINGO'
        print a
        break


