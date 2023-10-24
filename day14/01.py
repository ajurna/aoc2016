from copy import copy
from hashlib import md5
from collections import defaultdict
import regex


def get_hash(s):
    return md5(s).hexdigest()


def get_hash2(s):
    h = md5(s)
    for _ in range(2016):
        h = md5(h.hexdigest().encode())
    return h.hexdigest()


def search(key, hasher):
    triple = regex.compile(r'(?P<l>\w)(?P=l){2}')
    quintuple = regex.compile(r'(?P<l>\w)(?P=l){4}')
    idx = 0
    data = defaultdict(list)
    found = []
    while True:
        digest = hasher(key + str(idx).encode())
        for q in quintuple.findall(digest):
            for t in data[q]:
                if t > idx - 1001:
                    if t not in found:
                        found.append(t)
        if m := triple.search(digest):
            data[m.group(1)].append(idx)
        if len(found) > 64:
            return sorted(found)[63]
        idx += 1


print("Part 1: ", search(b'cuanljph', get_hash))
print("Part 2: ", search(b'cuanljph', get_hash2))
