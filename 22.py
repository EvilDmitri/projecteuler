#*-*coding=utf-8 *-8
"""


Используйте names.txt (правый клик и 'Save Link/Target As...'), текстовый файл размером 46 КБ,
содержащий более пяти тысяч имён. Начните с сортировки в алфавитном порядке.
Затем подсчитайте алфавитные значения каждого имени и умножьте это значение на порядковый номер имени
в отсортированном списке для получения количества очков имени.

Например, если список отсортирован по алфавиту, имя COLIN (алфавитное значение которого 3 + 15 + 12 + 9 + 14 = 53)
является 938-ым в списке. Поэтому, имя COLIN получает 938 × 53 = 49714 очков.

Какова сумма очков имён в файле?

"""


def get_names():
    names_list = []
    with open('names.txt', 'r') as names:
        line = names.readline()
        names_list = [b[1:-1] for b in line.split(',')]
        names_list.sort()
        return names_list


def count():
    names = get_names()

    total_score = 0
    for name in names:

        alpha_value = 0
        for char in name:
            alpha_value += ord(char) - 64

        name_score = alpha_value * (names.index(name)+1)
        print name, name_score

        total_score += name_score

    print total_score


count()








