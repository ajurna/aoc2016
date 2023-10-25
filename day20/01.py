from collections import deque
from typing import Deque

addresses = []
with open('01.txt') as f:
    for line in f.readlines():
        a, b = line.split('-')
        addresses.append(range(int(a), int(b)+1))
addresses.sort(key=lambda x: (x.start, x.stop), )


addresses: Deque[range] = deque(addresses)
grouped = deque([])
while True:
    r1 = addresses.popleft()
    r2 = addresses.popleft()
    if r1.stop >= r2.start:
        addresses.appendleft(range(r1.start, max(r1.stop, r2.stop)))
    else:
        grouped.append(r1)
        addresses.appendleft(r2)
        print("Part 1:", r1.stop)
        break

while addresses:
    r1 = addresses.popleft()
    try:
        r2 = addresses.popleft()
    except IndexError:
        grouped.append(r1)
        break
    if r1.stop >= r2.start:
        addresses.appendleft(range(r1.start, max(r1.stop, r2.stop)))
    else:
        grouped.append(r1)
        addresses.appendleft(r2)
total = 0
while grouped:
    g1 = grouped.popleft()
    g2 = grouped.popleft()
    total += len(range(g1.stop, g2.start))
    if len(grouped) == 0:
        break
    grouped.appendleft(g2)
print("Part 2:", total)
