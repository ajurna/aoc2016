from collections import Counter
import re
from string import ascii_lowercase

matcher = re.compile(r"(?P<name>[\w-]+)-(?P<sector>\d+)\[(?P<checksum>\w+)]")
score = 0
north_pole_sector = 0
with open("01.txt", 'r') as f:
    for line in f.readlines():
        match = matcher.match(line).groupdict()
        items = [(v, k) for k, v in Counter(match['name'].replace('-', '')).items()]
        items.sort(key=lambda x: (-x[0], x[1]))
        items = ''.join([x for _, x in items][:5])
        if items == match['checksum']:
            score += int(match['sector'])
        name = ''
        for letter in match['name']:
            if letter == '-':
                name += '-'
                continue
            name += ascii_lowercase[(ascii_lowercase.index(letter) + int(match['sector'])) % 26]
        if "north" in name:
            north_pole_sector = match['sector']
print("Part 1:", score)
print("Part 2:", north_pole_sector)



