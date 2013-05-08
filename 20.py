#*-*coding=utf-8 *-8
"""
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!

"""
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

digits = list(str(factorial(100)))

S = 0
for digit in digits:
    print(digit)
    S += int(digit)

print(S)