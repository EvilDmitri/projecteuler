def get_next(n):
    if n % 2 == 0:
        n /= 2
    else:
        n = 3 * n + 1
    return n

longest = [0, 0]
used_dict = dict()


def counter(start):
    global longest
    # if start in used_dict:
    #     return used_dict[start]

    count = 2
    a = get_next(start)
    # print a

    while not a == 1:
        a = get_next(a)
        # print a
        # if a in used_dict:
        #     return used_dict[a]

        count += 1

    # used_dict[a] = count
    if count > longest[1]:
        longest[1] = count
        longest[0] = start
    return count

# print ('x - %d' % counter(40))

for x in xrange(1, 1000000):
    print '-------'
    print ('%d - %d' % (x, counter(x)))

print '------------------------------'
print longest[0], ' - ', longest[1]

