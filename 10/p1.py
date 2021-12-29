import sys
from typing import Optional

assert len(sys.argv) > 1, "No input file given"
input_file_name = sys.argv[1]

lines = open(input_file_name).read().strip().split('\n')

ans = 0
_OPEN = "<{[("
_CLOSE = ">}])"
_ERROR_SCORES = {
  ")": 3, "]": 57, "}": 1197, ">": 25137
}
_KEYS = {
  "(": ")", ")": ")",
  "[": "]", "]": "]",
  "{": "}", "}": "}",
  "<": ">", ">": ">", 
}

# Actually we also need to track the last open, so let's just use a stack?

for i, line in enumerate(lines):
  counter = {x: 0 for x in _ERROR_SCORES}
  stack = []
  for i, char in enumerate(line):
    if char in _OPEN:
      stack.append(char)
    else:
      if _KEYS[stack[-1]] != char:
        ans += _ERROR_SCORES[char]
        # print(line, "----------", char, " --- ", i)
        break
      else:
        stack.pop()


print(ans)

# { ( [ ( < {} [ <> [] }>{[]{[(<()>
# [ ( { ( <(())[]> [ [ { [] { <()<>>