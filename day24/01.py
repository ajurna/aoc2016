import heapq
from collections import defaultdict, deque
from itertools import combinations, count
from typing import NamedTuple, Tuple


# spots = [0, 1, 2, 3, 4]
# for c in combinations(spots, 2):
#     print(c)

class Point(NamedTuple):
    x: int
    y: int

    def distance(self, target: "Point"):
        return abs(self.x - target.x) + abs(self.y - target.y)

    def __add__(self, other: "Point"):
        return Point(self.x + other.x, self.y + other.y)

    def neighbors(self):
        return [self + p for p in [Point(0, 1), Point(1, 0), Point(0, -1), Point(-1, 0)]]

    def score(self, places: Tuple["Point", ...]):
        distances = [self.distance(p) for p in places]
        return min(distances) + 0.1 * sum(distances)  # Adjust alpha (0.1 here) as per your problem's requirement

spots = {}
grid = []
with open('01.txt') as f:
    for y, line in enumerate(f.readlines()):
        new_line = []
        for x, pos in enumerate(line.strip()):
            if pos.isdigit():
                spots[int(pos)] = Point(x, y)
                new_line.append('.')
            else:
                new_line.append(pos)

        grid.append(new_line)
print(spots)

for row in grid:
    print(''.join(row))


def search(start, places_to_visit, area):
    queue = deque()
    # heapq.heapify(queue)
    c = count()
    queue.append((start, places_to_visit, 0))
    visited = defaultdict(set)
    visited[places_to_visit].add(start)
    while queue:
        position, remaining, steps = queue.popleft()
        position: Point
        steps += 1
        for choice in position.neighbors():
            if area[choice.y][choice.x] == '#':
                continue
            if choice in remaining:
                new_remaining = tuple(r for r in remaining if r != choice)
            else:
                new_remaining = remaining
            if choice in visited[new_remaining]:
                continue
            visited[new_remaining].add(choice)
            if len(new_remaining) == 0:
                return steps
            queue.append((choice, new_remaining, steps))



part1 = search(spots[0], tuple(s for k, s in spots.items() if k != 0), grid)
print(part1)