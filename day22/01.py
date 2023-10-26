from dataclasses import dataclass
import re
from typing import NamedTuple, List


@dataclass
class Node:
    size: int
    used: int

    @property
    def avail(self):
        return self.size - self.used


class Point(NamedTuple):
    x: int
    y: int

    def __add__(self, other: "Point"):
        return Point(self.x + other.x, self.y + other.y)

    def neighbors(self):
        return [self + p for p in [Point(0, 1), Point(1, 0), Point(0, -1), Point(-1, 0)]]


node_re = re.compile(
    r'/dev/grid/node-x(?P<x>\d+)-y(?P<y>\d+)\s+(?P<size>\d+)T\s+(?P<used>\d+)T\s+(?P<avail>\d+)T\s+(?P<use>\d+)%')

grid: List[List[Node, ...]] = []
for y in range(26):
    grid.append([[]] * 38)
all_nodes = []
with open('01.txt') as f:
    f.readline()
    f.readline()
    for line in f.readlines():
        if match := node_re.match(line):
            node = Node(int(match.group('size')), int(match.group('used')))
            grid[int(match.group('y'))][int(match.group('x'))] = node
            all_nodes.append(node)

total = 0
c = 0
for a in all_nodes:
    for b in all_nodes:
        c += 1
        if a.used == 0 or a == b:
            continue
        if b.avail > a.used:
            print(a, b)
            total += 1
print("Part 1:", total)

# Use the map generated to manually calculate the result.
for row in grid:
    row: List[Node]
    print(' '.join(f"{n.used:>3}|{n.size:<3}" for n in row))
