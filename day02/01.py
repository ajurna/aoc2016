from dataclasses import dataclass
from typing import NamedTuple

with open('01.txt') as f:
    directions = [l.strip() for l in f.readlines()]


class Point(NamedTuple):
    x: int
    y: int

    def __add__(self, other: "Point"):
        return Point(self.x + other.x, self.y + other.y)


@dataclass
class Navigation:
    x: int = 1
    y: int = 1

    def move(self, letter: str):
        match letter:
            case "U":
                self.y = max(self.y - 1, 0)
            case "D":
                self.y = min(self.y + 1, 2)
            case "L":
                self.x = max(self.x - 1, 0)
            case "R":
                self.x = min(self.x + 1, 2)


print(directions)
keypad = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
nav = Navigation()

result = []
for line in directions:
    for let in line:
        nav.move(let)
    result.append(keypad[nav.y][nav.x])
print(''.join(str(i) for i in result))

keypad = {
    Point(0, 2): "5",
    Point(1, 1): "2",
    Point(1, 2): "6",
    Point(1, 3): "A",
    Point(2, 0): "1",
    Point(2, 1): "3",
    Point(2, 2): "7",
    Point(2, 3): "B",
    Point(2, 4): "D",
    Point(3, 1): "4",
    Point(3, 2): "8",
    Point(3, 3): "C",
    Point(4, 2): "9",
}


@dataclass
class Navigation2:
    location: Point = Point(x=0, y=2)

    def move(self, letter):
        match letter:
            case "U":
                next_move = self.location + Point(0, -1)
            case "D":
                next_move = self.location + Point(0, 1)
            case "L":
                next_move = self.location + Point(-1, 0)
            case "R":
                next_move = self.location + Point(1, 0)
        if next_move in keypad.keys():
            self.location = next_move


nav = Navigation2()
result = []
for line in directions:
    for let in line:
        nav.move(let)
    result.append(keypad[nav.location])
print(''.join(str(i) for i in result))
