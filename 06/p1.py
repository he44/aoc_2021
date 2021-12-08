import sys
from typing import List

assert len(sys.argv) > 1, "No input file given"
input_file_name = sys.argv[1]

_POSSIBLE_STATES = [x for x in range(9)]
_DAYS= 256

fishes = [0 for x in _POSSIBLE_STATES]

lines = open(input_file_name).read().strip().split('\n')

for line in lines:
  for day in line.split(','):
    fishes[int(day)] += 1

def update(fishes: List[int]) -> List[int]:
  new_fishes = [0 for x in _POSSIBLE_STATES]
  # for fish with days from 1 to 8, just decresing
  for d in range(1, 9):
    new_fishes[d-1] = fishes[d]
  # for fish with days 0, they become 6
  new_fishes[6] += fishes[0]
  new_fishes[8] += fishes[0]
  return new_fishes



for day in range(_DAYS):
  fishes = update(fishes)

ans = sum(fishes)

print(ans)


