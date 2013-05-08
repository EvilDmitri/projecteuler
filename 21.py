#*-*coding=utf-8 *-8
"""


Пусть d(n) определяется как сумма делителей n (числа меньше n, делящие n нацело).
Если d(a) = b и d(b) = a, где a ≠ b, то a и b называются дружественной парой,
а каждое из чисел a и b - дружественным числом.

Например, делителями числа 220 являются 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 и 110, поэтому d(220) = 284.
Делители 284 - 1, 2, 4, 71, 142, поэтому d(284) = 220.

Посчитайте сумму всех дружественных чисел меньше 10000.

"""


def trying():

    used_numbers = []
    for num in range(28, 10000):
        a = count_sum_of_divisors(num)
        b = count_sum_of_divisors(a)
        if num == b and a != b:
            if not a in used_numbers:
                if not b in used_numbers:
                    used_numbers.append(a)
                    used_numbers.append(b)
                    #print used_numbers
    print sum(used_numbers)


def count_sum_of_divisors(number):
    sum_of_divisors = 0
    for x in range(1, number):
        if not number % x:
            sum_of_divisors += x

    return sum_of_divisors


trying()