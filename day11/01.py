import collections
import heapq
import itertools
from dataclasses import dataclass
from itertools import combinations, chain
from typing import List, Tuple

from frozendict import frozendict


@dataclass(frozen=True)
class Generator:
    type: str

    def __len__(self):
        return 1

    def __iter__(self):
        yield self


@dataclass(frozen=True)
class Chip:
    type: str

    def __len__(self):
        return 1

    def __iter__(self):
        yield self


@dataclass
class State:
    state: frozendict[int, Tuple]
    elevator: int = 1
    moves: int = 0

    def valid(self):
        for floor in self.state.values():
            chips = [c for c in floor if isinstance(c, Chip)]
            generators = [g for g in floor if isinstance(g, Generator)]
            if len(chips) == 0 or len(generators) == 0:
                continue
            for chip in chips:
                if not any([g.type == chip.type for g in generators]):
                    return False
        return True

    def solved(self):
        return len(self.state[1]) == 0 and len(self.state[2]) == 0 and len(self.state[3]) == 0

    def get_valid_floors(self) -> List[int]:
        match self.elevator:
            case 1:
                return [2]
            case 2:
                if len(self.state[1]) == 0:
                    return [3]
                return [1, 3]
            case 3:
                if len(self.state[1]) == 0 and len(self.state[2]) == 2:
                    return [4]
                return [2, 4]
            case 4:
                return [3]


# site = frozendict({
#     1: (Chip("Hydrogen"), Chip('lithium')),
#     2: (Generator("Hydrogen"),),
#     3: (Generator("lithium"),),
#     4: (),
# })

part1 = State(frozendict({
    1: (Generator('polonium'), Generator('thulium'), Chip('thulium'), Generator('promethium'), Generator('ruthenium'),
        Chip('ruthenium'), Generator('cobalt'), Chip('cobalt')),
    2: (Chip('polonium'), Chip('promethium')),
    3: (),
    4: (),
}))

part2 = State(frozendict({
    1: (Generator('polonium'), Generator('thulium'), Chip('thulium'), Generator('promethium'), Generator('ruthenium'),
        Chip('ruthenium'), Generator('cobalt'), Chip('cobalt'), Generator('elerium'), Chip('elerium'),
        Generator('dilithium'), Chip('dilithium')),
    2: (Chip('polonium'), Chip('promethium')),
    3: (),
    4: (),
}))


def heuristic(state):
    """Estimate the number of moves required to reach the goal. This assumes every object requires
    two moves to reach the fourth floor (one to pick it up and one to drop it off), minus one if the elevator
    is already on its floor, and minus one more if the elevator can carry it along with another object."""
    total_moves = 0
    for floor, items in state.state.items():
        n_items = len(items)
        total_moves += (4 - floor) * 2 * n_items  # two moves are required for each item to reach the 4th floor
        if floor == state.elevator:
            total_moves -= 1  # minus one if the elevator is already on the object's floor
        if n_items >= 2 or (state.elevator == floor and n_items >= 1):
            total_moves -= 1  # minus one more if the elevator can carry it along with another object

    return total_moves


def canonical(elevator, state):
    floors = []
    for floor in state.values():
        counter = collections.Counter()
        for item in floor:
            counter[item.type] += 1
        floors.append(tuple(sorted(counter.items())))
    return elevator, tuple(floors)


def search(state):
    count = itertools.count()
    queue = []
    heapq.heappush(queue, (0, next(count), state))  # States are now sorted by their moves
    visited = set()
    visited.add(canonical(state.elevator, state.state))

    while queue:
        _, _, current = heapq.heappop(queue)  # get state with min heuristic value
        if current.solved():
            return current.moves  # current is already solved return number of moves
        for move in chain(current.state[current.elevator], combinations(current.state[current.elevator], 2)):
            for floor in current.get_valid_floors():
                new_state = {k: v for k, v in current.state.items()}
                for item in move:
                    new_state[floor] = new_state[floor] + (item,)
                    new_state[current.elevator] = tuple([i for i in new_state[current.elevator] if i != item])
                new_state = frozendict(new_state)
                canon_new_state = canonical(floor, new_state)
                if canon_new_state in visited:
                    continue
                visited.add(canon_new_state)
                next_move = State(
                    state=new_state,
                    elevator=floor,
                    moves=current.moves + 1
                )
                if next_move.valid():
                    estimate = next_move.moves + heuristic(next_move)
                    heapq.heappush(queue, (estimate, next(count), next_move))


print(search(part1))
print(search(part2))
