#*-*coding=utf-8 *-8
"""


Число 3797 обладает интересным свойством. Будучи само по себе простым числом, из него можно последовательно
выбрасывать цифры слева направо, число же при этом остается простым на каждом этапе: 3797, 797, 97, 7.
Точно таким же способом можно выбрасывать цифры справа налево: 3797, 379, 37, 3.

Найдите сумму единственных одиннадцати простых чисел, из которых можно выбрасывать цифры как справа налево,
так и слева направо, но числа при этом остаются простыми.

ПРИМЕЧАНИЕ: числа 2, 3, 5 и 7 таковыми не считаются.



40 простых чисел
n*n - 79*n + 1601 (n = 0 -- 79)
"""


primes = []
with open('primes.txt', 'r') as f:
    primes = [x.strip() for x in f.readlines()]


def check_number(number):
    str_number = str(number)
    for x in range(1, str_number.__len__()):
        if str_number[x:] in primes:
            pass
        else:
            break



for digit in primes:
    pass