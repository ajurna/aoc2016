from collections import Counter
with open("01.txt", 'r') as f:
    data = [list(l.strip()) for l in f.readlines()]

part1 = ""
part2 = ""
for i in range(len(data[0])):
    counts = {v: k for k, v in Counter([x[i] for x in data]).items()}
    part1 += counts[max(counts)]
    part2 += counts[min(counts)]
print("Part 1:", part1)
print("Part 2:", part2)