commands = []

with open("01.txt") as f:
    for line in f.readlines():
        if line.startswith('cpy'):
            c, a, b = line.split()
            if a.isdigit():
                a = int(a)
            commands.append((c, a, b))
        elif line.startswith('inc'):
            c, a = line.split()
            commands.append((c, a))
        elif line.startswith('dec'):
            c, a = line.split()
            commands.append((c, a))
        elif line.startswith('jnz'):
            c, a, b = line.split()
            if a.isdigit():
                a = int(a)
            b = int(b)
            commands.append((c, a, b))


def get_val(val, registers):
    if val in registers:
        return registers[val]
    return val


def run(program, registers):
    pointer = 0
    while pointer < len(program):
        command = program[pointer]
        match command[0]:
            case 'cpy':
                registers[command[2]] = get_val(command[1], registers)
            case 'inc':
                registers[command[1]] += 1
            case 'dec':
                registers[command[1]] -= 1
            case 'jnz':
                if get_val(command[1], registers) != 0:
                    pointer += command[2]
                    continue
        pointer += 1
    return registers


print("Part 1:", run(commands, {
        'a': 0,
        'b': 0,
        'c': 0,
        'd': 0
    })['a'])

print("Part 2:", run(commands, {
        'a': 0,
        'b': 0,
        'c': 1,
        'd': 0
    })['a'])
