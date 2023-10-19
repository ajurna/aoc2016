from collections import defaultdict
from dataclasses import dataclass, field
from typing import List, Dict
import re


@dataclass
class Bot:
    id: int
    lower_target_type: str = "bot"
    lower_target_id: int = 0
    higher_target_type: str = "bot"
    higher_target_id: int = 0
    storage: List = field(default_factory=list)


bots: Dict[int, Bot] = {}
output: Dict[int, List] = defaultdict(list)
part1 = 0

with open('01.txt') as f:
    for line in f.readlines():
        line = line.strip()
        if match := re.match(r"value (?P<value>\d+) goes to bot (?P<bot>\d+)", line):
            value, bot_id = map(int, match.groups())
            if bot_id in bots:
                bot = bots[bot_id]
            else:
                bot = Bot(bot_id)
                bots[bot_id] = bot
            bot.storage.append(value)
        elif match := re.match(r"bot (?P<bot_id>\d+) gives low to (?P<low_out>\w+) (?P<low_id>\d+) and high to (?P<high_out>\w+) (?P<high_id>\d+)", line):
            bot_id = int(match.group('bot_id'))
            if bot_id in bots:
                bot = bots[bot_id]
            else:
                bot = Bot(bot_id)
                bots[bot_id] = bot
            bot.lower_target_id = int(match.group('low_id'))
            bot.lower_target_type = match.group('low_out')
            bot.higher_target_id = int(match.group('high_id'))
            bot.higher_target_type = match.group('high_out')
        else:
            print(line)


def process_bot(bot: Bot):
    global part1
    high = max(bot.storage)
    low = min(bot.storage)
    if 61 in bot.storage and 17 in bot.storage:
        part1 = bot.id
    if bot.higher_target_type == 'bot':
        while len(bots[bot.higher_target_id].storage) == 2:
            process_bot(bots[bot.higher_target_id])
        bots[bot.higher_target_id].storage.append(high)
    else:
        output[bot.higher_target_id].append(high)
    if bot.lower_target_type == "bot":
        while len(bots[bot.lower_target_id].storage) == 2:
            process_bot(bots[bot.lower_target_id])
        bots[bot.lower_target_id].storage.append(low)
    else:
        output[bot.lower_target_id].append(low)
    bot.storage.clear()


while targets := [b for b in bots.values() if len(b.storage) == 2]:
    process_bot(targets[0])

print("Part 1:", part1)
print("Part 2:", output[0][0] * output[1][0] * output[2][0])
