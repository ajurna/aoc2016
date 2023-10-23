from collections import deque
from heapq import heapify, heappop, heappush
from itertools import count
from typing import NamedTuple


class Point(NamedTuple):
    x: int
    y: int

    def __add__(self, other: "Point"):
        return Point(self.x + other.x, self.y + other.y)

    def distance(self, target: "Point"):
        return abs(self.x - target.x) + abs(self.y - target.y)

    def is_wall(self, fav: int):
        cal = bin((self.x * self.x + 3 * self.x + 2 * self.x * self.y + self.y + self.y * self.y) + fav).count('1')
        return True if cal % 2 == 1 else False

    def neighbors(self):
        return [self+p for p in [Point(0, 1), Point(1, 0), Point(0, -1), Point(-1, 0)]]

    def moves(self, fav: int):
        out = []
        for neighbor in self.neighbors():
            if neighbor.x < 0 or neighbor.y < 0:
                continue
            if neighbor.is_wall(fav):
                continue
            out.append(neighbor)
        return out


def search(start: Point, end: Point, fav: int):
    queue = []
    heapify(queue)
    counter = count()
    heappush(queue, (start.distance(end), next(counter), start, 0))
    visited = set()
    visited.add(start)
    while queue:
        _, _, position, steps = heappop(queue)
        steps += 1
        for move in position.moves(fav):
            if move == end:
                return steps, visited
            if move in visited:
                continue
            visited.add(move)
            heappush(queue, (move.distance(end), next(counter), move, steps))


def search2(start: Point, fav: int):
    counter = count()
    queue = deque()
    queue.append((start, 0))
    visited = set()
    visited.add(start)
    while queue:
        position, steps = queue.popleft()
        steps += 1
        if steps > 50:
            continue
        for move in position.moves(fav):

            if move in visited:
                continue
            visited.add(move)
            queue.append((move, steps))
    return len(visited)


print("Part 1:", search(Point(1, 1), Point(31, 39), 1350)[0])
print("Part 2:", search2(Point(1, 1), 1350))
