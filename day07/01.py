import re
abba_in_hyper_net = re.compile(r"\[[^]]*(?P<first>\w)(?!(?P=first))(?P<second>\w)(?P=second)(?P=first)[^]]*]")
abba_outside_hyper_net = re.compile(r"(?P<first>\w)(?!(?P=first))(?P<second>\w)(?P=second)(?P=first)")
aba = re.compile(r"\[[^]]*(?P<third>\w)(?!(?P=third))(?P<forth>\w)(?P=third)[^]]*](?:[^][\n]+\[[^]]*])*(?P=forth)(?P=third)(?P=forth)")


def find_sequences(net):
    """Find aba patterns in given net."""
    sequences = []
    for i in range(len(net) - 2):
        triplet = net[i:i + 3]
        if triplet[0] == triplet[2] and triplet[0] != triplet[1]:
            sequences.append(triplet)
    return sequences


def supports_ssl(s):
    # Split the string into supernets and hypernets
    parts = s.split('[')
    supernets = [parts[0]]
    hypernets = []

    for part in parts[1:]:
        hypernet, supernet = part.split(']')
        supernets.append(supernet)
        hypernets.append(hypernet)

    supernet_seqs = [seq for net in supernets for seq in find_sequences(net)]
    hypernet_seqs = [seq for net in hypernets for seq in find_sequences(net)]

    # Check for matching sequences
    for seq in supernet_seqs:
        reverse_seq = seq[1] + seq[0] + seq[1]
        if reverse_seq in hypernet_seqs:
            return True

    for seq in hypernet_seqs:
        reverse_seq = seq[1] + seq[0] + seq[1]
        if reverse_seq in supernet_seqs:
            return True

    return False


part1 = 0
part2 = 0
with open('01.txt') as f:
    for line in f.readlines():
        line = line.strip()
        if abba_outside_hyper_net.search(line) and not abba_in_hyper_net.search(line):
            part1 += 1
        if supports_ssl(line):
            part2 += 1

print("Part 1:", part1)
print("Part 2:", part2)
