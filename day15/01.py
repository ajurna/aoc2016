from typing import NamedTuple
from itertools import count


class Disk(NamedTuple):
    size: int
    state: int

    def open(self, tick):
        return (self.state + tick) % self.size == 0


def search(disks):
    c = count()
    while True:
        t = next(c)
        if all(d.open(i+t) for d, i in zip(disks, count(1))):
            return t


print("Part 1:", search([Disk(17, 15), Disk(3, 2), Disk(19, 4), Disk(13, 2), Disk(7, 2), Disk(5, 0)]))
print("Part 2:", search([Disk(17, 15), Disk(3, 2), Disk(19, 4), Disk(13, 2), Disk(7, 2), Disk(5, 0), Disk(11, 0)]))
