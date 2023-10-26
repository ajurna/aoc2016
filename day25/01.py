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
        elif line.startswith('out'):
            c, a = line.split()
            commands.append((c, a))


class Computer:
    def __init__(self, program, a=0, b=0, c=0, d=0):
        self.pointer = 0
        self.program = program
        self.registers = {
            'a': a,
            'b': b,
            'c': c,
            'd': d
        }

    def get_val(self, val):
        if val in self.registers:
            return self.registers[val]
        return val

    def run(self):
        while self.pointer < len(self.program):
            command = self.program[self.pointer]
            match command[0]:
                case 'out':
                    self.pointer += 1
                    return self.get_val(command[1])
                case 'cpy':
                    self.registers[command[2]] = self.get_val(command[1])
                case 'inc':
                    self.registers[command[1]] += 1
                case 'dec':
                    self.registers[command[1]] -= 1
                case 'jnz':
                    if self.get_val(command[1]) != 0:
                        self.pointer += self.get_val(command[2])
                        continue
            self.pointer += 1


part1 = 0
while True:
    com = Computer(commands, a=part1)
    result = [com.run() for _ in range(16)]
    if result == [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]:
        break
    part1 += 1

print("Part 1:", part1)
