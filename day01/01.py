from dataclasses import dataclass, field
from typing import Tuple, Dict, Set, NamedTuple, Optional

with open('01.txt') as f:
    directions = f.read().strip().split(', ')


class Point(NamedTuple):
    x: int
    y: int

    def distance(self, target: "Point"):
        return abs(self.x - target.x) + abs(self.y - target.y)


@dataclass
class Navigation:
    x: int = 0
    y: int = 0
    orientation: str = 'N'
    orientations: Tuple[str, ...] = ("N", "E", "S", "W")
    directions: Dict = field(default_factory=dict)
    visited: Set = field(default_factory=set)
    twice_visited: Optional[Point] = None

    def __post_init__(self):
        self.directions = {
            "N": Point(0, 1),
            "E": Point(1, 0),
            "S": Point(0, -1),
            "W": Point(-1, 0)
        }
        self.visited.add(Point(0, 0))

    def move(self, detail):
        direction, distance = detail[0], int(detail[1:])
        or_idx = self.orientations.index(self.orientation)
        match direction:
            case 'R':
                try:
                    self.orientation = self.orientations[or_idx + 1]
                except IndexError:
                    self.orientation = self.orientations[0]
            case 'L':
                self.orientation = self.orientations[or_idx - 1]
        for _ in range(distance):
            self.x += self.directions[self.orientation][0]
            self.y += self.directions[self.orientation][1]
            new_point = Point(self.x, self.y)
            if not self.twice_visited:
                if new_point in self.visited:
                    self.twice_visited = new_point
                else:
                    self.visited.add(new_point)

    def distance(self, target: Point):
        return abs(self.x - target.x) + abs(self.y - target.y)


n = Navigation()
for move in directions:
    n.move(move)
print("Part 1:", n.distance(Point(0, 0)))
print("Part 2:", n.twice_visited.distance(Point(0, 0)))
