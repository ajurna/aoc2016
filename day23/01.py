import math

commands = []

with open("01.txt") as f:
    for line in f.readlines():
        if line.startswith('cpy'):
            c, a, b = line.split()
            try:
                a = int(a)
            except ValueError:
                pass
            try:
                b = int(b)
            except ValueError:
                pass
            commands.append((c, a, b))
        elif line.startswith('inc'):
            c, a = line.split()
            commands.append((c, a))
        elif line.startswith('dec'):
            c, a = line.split()
            commands.append((c, a))
        elif line.startswith('jnz'):
            c, a, b = line.split()
            try:
                a = int(a)
            except ValueError:
                pass
            try:
                b = int(b)
            except ValueError:
                pass
            commands.append((c, a, b))
        elif line.startswith('tgl'):
            c, a = line.split()
            commands.append((c, a))


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
                    pointer += get_val(command[2], registers)
                    continue
            case 'tgl':
                idx = get_val(command[1], registers)
                try:
                    subcommand = program[pointer+idx]
                    match subcommand[0]:
                        case 'cpy':
                            program[pointer+idx] = ('jnz', subcommand[1], subcommand[2])
                        case 'jnz':
                            program[pointer+idx] = ('cpy', subcommand[1], subcommand[2])
                        case 'inc':
                            program[pointer+idx] = ('dec', subcommand[1])
                        case 'dec':
                            program[pointer+idx] = ('inc', subcommand[1])
                        case 'tgl':
                            program[pointer+idx] = ('inc', subcommand[1])
                except IndexError:
                    pass
        pointer += 1
    return registers


part1 = run(commands, {
        'a': 7,
        'b': 0,
        'c': 0,
        'd': 0
    })

print("Part 1:", part1['a'])

difference = part1['a'] - math.factorial(7)

part2 = math.factorial(12) + difference

print("Part 2:", part2)
