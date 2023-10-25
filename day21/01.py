import re


with open('01.txt') as f:
    data = f.readlines()


def process_password(password: str, steps):
    pw = [*password]
    for line in steps:
        if match := re.match(r'swap position (?P<x>\d+) with position (?P<y>\d+)', line):
            x, y = map(int, match.groups())
            t = pw[x]
            pw[x] = pw[y]
            pw[y] = t
        elif match := re.match(r'swap letter (?P<x>\w+) with letter (?P<y>\w+)', line):
            x, y = match.groups()
            xp, yp = pw.index(x), pw.index(y)
            pw[xp] = y
            pw[yp] = x
        elif match := re.match(r'reverse positions (?P<x>\w+) through (?P<y>\w+)', line):
            x, y = map(int, match.groups())
            pw = pw[:x] + pw[x:y + 1][::-1] + pw[y + 1:]
        elif match := re.match(r'rotate (?P<d>left|right) (?P<x>\w+) steps?', line):
            d, x = match.group('d'), int(match.group('x'))
            if d == "left":
                for _ in range(x):
                    pw = pw[1:] + [pw[0]]
            if d == "right":
                for _ in range(x):
                    pw = [pw[-1]] + pw[:-1]
        elif match := re.match(r'move position (?P<x>\w+) to position (?P<y>\w+)', line):
            x, y = map(int, match.groups())
            xl = pw[x]
            del pw[x]
            pw.insert(y, xl)
        elif match := re.match(r'rotate based on position of letter (?P<x>\w+)', line):
            x = match.group('x')
            xi = pw.index(x)
            if xi >= 4:
                xi += 1
            xi += 1
            for _ in range(xi):
                pw = [pw[-1]] + pw[:-1]
        else:
            print(line)
    return ''.join(pw)


def reverse_password(password: str, steps):
    pw = [*password]
    for line in steps:
        if match := re.match(r'swap position (?P<x>\d+) with position (?P<y>\d+)', line):
            x, y = map(int, match.groups())
            t = pw[x]
            pw[x] = pw[y]
            pw[y] = t
        elif match := re.match(r'swap letter (?P<x>\w+) with letter (?P<y>\w+)', line):
            x, y = match.groups()
            xp, yp = pw.index(x), pw.index(y)
            pw[xp] = y
            pw[yp] = x
        elif match := re.match(r'reverse positions (?P<x>\w+) through (?P<y>\w+)', line):
            x, y = map(int, match.groups())
            pw = pw[:x] + pw[x:y + 1][::-1] + pw[y + 1:]
        elif match := re.match(r'rotate (?P<d>left|right) (?P<x>\w+) steps?', line):
            d, x = match.group('d'), int(match.group('x'))
            if d == "right":
                for _ in range(x):
                    pw = pw[1:] + [pw[0]]
            else:
                for _ in range(x):
                    pw = [pw[-1]] + pw[:-1]
        elif match := re.match(r'move position (?P<x>\w+) to position (?P<y>\w+)', line):
            x, y = map(int, match.groups())
            yl = pw[y]
            del pw[y]
            pw.insert(x, yl)
        elif match := re.match(r'rotate based on position of letter (?P<x>\w+)', line):
            x = match.group('x')
            xi = pw.index(x)
            for _ in range({
                0: 1,
                1: 1,
                2: 6,
                3: 2,
                4: 7,
                5: 3,
                6: 0,
                7: 4
            }[xi]):
                pw = pw[1:] + [pw[0]]
        else:
            print(line)
    return ''.join(pw)


print("Part 1:", process_password('abcdefgh', data))
print("Part 2:", reverse_password('fbgdceah', data[::-1]))
