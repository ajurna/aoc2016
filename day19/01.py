from dataclasses import dataclass
from collections import deque
from typing import Deque


@dataclass
class Elf:
    id: int
    presents: int = 1


def search(elf_count):
    elves: Deque[Elf] = deque([Elf(e) for e in range(1, elf_count+1)])
    while len(elves) > 1:
        elf1 = elves.popleft()
        elf2 = elves.popleft()
        elf1.presents += elf2.presents
        elves.append(elf1)
    return elves.popleft().id


def search2(elf_count):
    elves1: Deque[Elf] = deque([Elf(e) for e in range(1, elf_count//2+1)])
    elves2: Deque[Elf] = deque([Elf(e) for e in range(elf_count//2+1, elf_count+1)])
    while len(elves1) + len(elves2) > 1:
        e1 = elves1.popleft()
        e2 = elves2.popleft()
        if (len(elves2) + len(elves1)) % 2 == 1 and (len(elves2) + len(elves1)) > 0:
            elves1.append(elves2.popleft())
        e1.presents += e2.presents
        elves2.append(e1)
    return elves2.popleft().id


print("Part 1:", search(3018458))
print("Part 2:", search2(3018458))
