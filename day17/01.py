from collections import deque
from hashlib import md5
from typing import NamedTuple


class Point(NamedTuple):
    x: int
    y: int

    def __add__(self, other: "Point"):
        return Point(self.x + other.x, self.y + other.y)

    def neighbors(self):
        u = self + Point(0, -1)
        d = self + Point(0, 1)
        l = self + Point(-1, 0)
        r = self + Point(1, 0)
        return [u if u.y >= 0 else None, d if d.y <= 3 else None,l if l.x >= 0 else None,r if r.x <= 3 else None]


def search(passcode, start, end):
    queue = deque()
    queue.append((start, passcode.encode()))
    while queue:
        current, code = queue.popleft()
        digest = md5(code).hexdigest()
        for neighbour, door, direction in zip(current.neighbors(), digest, 'UDLR'):
            if neighbour and door in 'bcdef':
                new_code = code + direction.encode()
                if neighbour == end:
                    return new_code[len(passcode):].decode()
                queue.append((neighbour, new_code))


def search2(passcode, start, end):
    queue = deque()
    queue.append((start, passcode.encode()))
    longest = 0
    while queue:
        current, code = queue.popleft()
        digest = md5(code).hexdigest()
        for neighbour, door, direction in zip(current.neighbors(), digest, 'UDLR'):
            if neighbour and door in 'bcdef':
                new_code = code + direction.encode()
                if neighbour == end:
                    if len(new_code[len(passcode):]) > longest:
                        longest = len(new_code[len(passcode):])
                    continue
                queue.append((neighbour, new_code))
    return longest


print("Part 1:", search("pxxbnzuo", Point(0, 0), Point(3, 3)))
print("Part 2:", search2("pxxbnzuo", Point(0, 0), Point(3, 3)))