# Looks like a context-free grammar? Maybe there's a smarter way doing this
# problem using CFG?

# Need to do some optimization otherwise it's too slow.
# Getting to step 24 would take 5 minutes.
import sys
from typing import List, Dict, Tuple

assert len(sys.argv) > 1, "No input file given"
input_file_name = sys.argv[1]

lines = open(input_file_name).read().strip().split('\n')

ans = 0
insertion_rules = {}
for i, line in enumerate(lines):
  if not line:
    continue
  if line.find(" -> ") != -1:
    src, dst = line.split(" -> ")
    insertion_rules[src] = (src[0] + dst, dst + src[1])
  else:
    initial_pattern = line

def ApplyRule(cur_counter: Dict[str, int], rules: Dict[str, Tuple[str, str]]) -> Dict[str, int]:
  new_counter = dict()
  for pattern in cur_counter:
    # only update the first pattern after insertion
    new_counter[rules[pattern][0]] = (new_counter.get(rules[pattern][0], 0) + 
                                      cur_counter[pattern])
    new_counter[rules[pattern][1]] = (new_counter.get(rules[pattern][1], 0) + 
                                      cur_counter[pattern])
  return new_counter

def ComputeRange(cur_counter: Dict[str, int]) -> int:
  letters_count = {}
  for pattern, count in cur_counter.items():
    # only counting the first char (because all the second chars will be
    # counted twice)
    char = pattern[0]
    letters_count[char] = letters_count.get(char, 0) + count
    # char = pattern[1]
    # letters_count[char] = letters_count.get(char, 0) + count
  # The last char would be the exception. All the insertions happen before it.
  letters_count[initial_pattern[-1]] += 1
  max_count = 0
  min_count = float('inf')
  for char, count in letters_count.items():
    max_count = max(max_count, count)
    min_count = min(min_count, count)
  print(letters_count)
  return max_count - min_count

print(initial_pattern)
print(insertion_rules)
counter = {}
for i in range(len(initial_pattern) - 1):
  pattern = initial_pattern[i:i+2]
  counter[pattern] = counter.get(pattern, 0) + 1
print(counter)

_STEPS = 40
for i in range(_STEPS):
  print(f"Finished step {i + 1}")
  counter = ApplyRule(counter, insertion_rules)
  # print(f"After step {i + 1}, {''.join(pattern)}")

ans = ComputeRange(counter)
print(ans)


