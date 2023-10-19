from collections import deque

with open('01.txt') as f:
    data_raw = f.read().strip()
    data_deque = deque(data_raw)


def decompress(data):
    decompressed = []
    while data:
        char = data.popleft()
        if char == "(":
            length = ""
            next_char = data.popleft()
            while next_char != 'x':
                length += next_char
                next_char = data.popleft()
            length = int(length)
            next_char = data.popleft()
            repeats = ''
            while next_char != ')':
                repeats += next_char
                next_char = data.popleft()
            repeats = int(repeats)
            buffer = ''
            for _ in range(length):
                buffer += data.popleft()
            decompressed.append(buffer*repeats)
        else:
            decompressed.append(char)
    return ''.join(decompressed)


def get_length(enc: str) -> int:
    if '(' not in enc:
        return len(enc)
    total_length = 0
    while '(' in enc:
        marker_start = enc.index('(')
        marker_end = enc.index(')')
        total_length += marker_start
        length, repeats = map(int, enc[marker_start + 1:marker_end].split('x'))
        buffer = enc[marker_end + 1:marker_end + length + 1]
        total_length += get_length(buffer) * repeats
        enc = enc[marker_end + length + 1:]
    total_length += len(enc)
    return total_length


print("Part 1:", len(decompress(data_deque)))
print("Part 2:", get_length(data_raw))
