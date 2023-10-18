import re
screen = [
    [' '] * 50,
    [' '] * 50,
    [' '] * 50,
    [' '] * 50,
    [' '] * 50,
    [' '] * 50,
]


def draw_screen(s):
    for r in s:
        print(''.join(r))


with open('01.txt', 'r') as f:
    for line in f.readlines():
        if match := re.match(r"rect (?P<x>\d+)x(?P<y>\d+)", line):
            for y in range(int(match.group('y'))):
                for x in range(int(match.group('x'))):
                    screen[y][x] = '#'
        elif match := re.match(r"rotate column x=(?P<col>\d+) by (?P<dis>\d+)", line):
            col = []
            for row in screen:
                col.append(row[int(match.group('col'))])
            for _ in range(int(match.group('dis'))):
                col.insert(0, col.pop())
            for row in screen:
                row[int(match.group('col'))] = col.pop(0)
        elif match := re.match(r"rotate row y=(?P<row>\d+) by (?P<dis>\d+)", line):
            row = int(match.group('row'))
            for _ in range(int(match.group('dis'))):
                screen[row].insert(0, screen[row].pop())
print("Part 1:", sum([x.count('#') for x in screen]))
print("Part 2:")
draw_screen(screen)