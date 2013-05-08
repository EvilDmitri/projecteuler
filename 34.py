#*-*coding=utf-8 *-8
"""

145 является любопытным числом, поскольку 1! + 4! + 5! = 1 + 24 + 120 = 145.

Найдите сумму всех чисел, каждое из которых равно сумме факториалов своих цифр.

Примечание: поскольку 1! = 1 и 2! = 2 не являются суммами, учитывать их не следует.


"""

from math import factorial


def count_factorial_sum(number):
    fac_sum = 0
    for digit in str(number):
        fac_sum += factorial(int(digit))
    return fac_sum

all_sum = 0
for num in xrange(3, 1000000):
    if count_factorial_sum(num) == num:
        all_sum += num
        print all_sum

print 'Ready', all_sum




