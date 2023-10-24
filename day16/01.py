from itertools import batched


def dragon(a):
    b = ['0' if i == '1' else '1' for i in a[::-1]]
    return a + '0' + ''.join(b)


def checksum(s):
    check = []
    for a, b in batched(s, 2):
        if a == b:
            check.append('1')
        else:
            check.append('0')
    check = ''.join(check)
    if len(check) % 2 == 0:
        return checksum(check)
    else:
        return check


def fill(data, size):
    while len(data) < size:
        data = dragon(data)
    return checksum(data[:size])


print("Part 1:", fill('00111101111101000', 272))
print("Part 1:", fill('00111101111101000', 35651584))
