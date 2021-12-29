# Looks like a context-free grammar? Maybe there's a smarter way doing this
# problem using CFG?
import sys
from typing import List

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
    insertion_rules[src] = dst
  else:
    initial_pattern = line


def ApplyRule(cur_pattern: List[str], rules: dict) -> str:
  new_pattern = []
  prev_in = False
  for i in range(len(cur_pattern) - 1):
    key = ''.join(cur_pattern[i:i+2])
    if key in rules:
      if not prev_in:
        new_pattern.append(key[0])
      new_pattern.append(rules[key])
      new_pattern.append(key[1])
      prev_in = True
    else:
      prev_in = False
  return new_pattern

def Range(cur_pattern: List[str]) -> int:
  counter = {}
  for char in cur_pattern:
    counter[char] = counter.get(char, 0) + 1
  max_count = 0
  min_count = len(cur_pattern)
  for char in cur_pattern:   
    max_count = max(counter[char], max_count)
    min_count = min(counter[char], min_count)
  return max_count - min_count

pattern = list(initial_pattern)
for i in range(10):
  pattern = ApplyRule(pattern, insertion_rules)
  # print(f"After step {i + 1}, {''.join(pattern)}")

ans = Range(pattern)
print(ans)


