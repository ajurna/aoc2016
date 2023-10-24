data = '^.^^^.^..^....^^....^^^^.^^.^...^^.^.^^.^^.^^..^.^...^.^..^.^^.^..^.....^^^.^.^^^..^^...^^^...^...^.'
data = [r == '^' for r in data]


def map_it_out(row, steps):
    result = row.count(False)
    for _ in range(steps):
        new_row = []
        if row[0] and row[1]:
            new_row.append(True)
        elif row[1]:
            new_row.append(True)
        else:
            new_row.append(False)
        for i in range(1, len(row)-1):
            match row[i-1:i+2]:
                case [True, True, False]:
                    new_row.append(True)
                case [False, True, True]:
                    new_row.append(True)
                case [True, False, False]:
                    new_row.append(True)
                case [False, False, True]:
                    new_row.append(True)
                case _:
                    new_row.append(False)
        if row[-2] and row[-1]:
            new_row.append(True)
        elif row[-2]:
            new_row.append(True)
        else:
            new_row.append(False)
        row = new_row
        result += row.count(False)
    return result


print("Part 1:", map_it_out(data, 39))
print("Part 2:", map_it_out(data, 399999))
