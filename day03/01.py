data = []
with open("01.txt", "r") as f:
    for line in f.readlines():
        data.append(list(map(int, line.split())))
count = 0
for line in data:
    a, b, c = sorted(line)
    if a + b > c:
        count += 1
print("Part 1:", count)
data_transpose = []
for batch_idx in range(0, len(data), 3):
    tri_slice = data[batch_idx:batch_idx + 3]
    data_transpose.extend([
        [tri_slice[0][0], tri_slice[1][0], tri_slice[2][0]],
        [tri_slice[0][1], tri_slice[1][1], tri_slice[2][1]],
        [tri_slice[0][2], tri_slice[1][2], tri_slice[2][2]],
    ])
count = 0
for line in data_transpose:
    a, b, c = sorted(line)
    if a+b > c:
        count += 1
print("Part 2:", count)
