"""
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
"""

from __future__ import print_function


def count(the_sum):
    string = str(the_sum)
    digits = list(string)

    the_sum = 0
    for dig in digits:
        the_sum += int(dig)
        print(dig, end='')
    print('\n')
    return the_sum


print(count(pow(2,1000)))
