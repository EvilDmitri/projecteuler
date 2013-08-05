# coding=utf-8
# create matrix
matrix = []
with open('table.txt') as f:
    for line in f:
        stroke = [int(x) for x in line.strip().split(' ')]
        matrix.append(stroke)

biggest = 0
# now we need to find greatest product of four adjacent numbers in the same direction
# (up, down, left, right, or diagonally) in the 20×20 grid?



def left_to_right():
    global biggest
    for line in matrix:
        summa = 1
        for i in range(20):
            for x in range(4):
                try :
                    summa *= line[i + x]
                except IndexError:
                    pass

            if summa > biggest:
                biggest = summa
            summa = 1


def up_to_down():
    global biggest
    summa = 1
    for i in range(20):
        for n in range(20):
            for m in range(4):
                try:
                    summa *= matrix[n+m][i]
                except IndexError:
                    pass
            if summa > biggest:
                biggest = summa
            summa = 1

left_to_right()
print biggest
up_to_down()
print biggest

print '---------------'

def diagonal_down():
    global biggest
    summa = 1
    for i in range(20):
        for n in range(20):
            for m in range(4):
                try:
                    summa *= matrix[i+m][n+m]
                except IndexError:
                    pass

            if summa > biggest:
                biggest = summa
            summa = 1

diagonal_down()
print biggest

print '------------'
def diagonal_up():
    global biggest
    summa = 1

    for i in range(20, 0, -1):

        for n in range(20):

            for m in range(4):

                try:
                    summa *= matrix[i - m][n + m]
                except IndexError:
                    pass

            if summa > biggest:
                biggest = summa
            summa = 1

diagonal_up()
print biggest





