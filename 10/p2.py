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
_COMPLETION_SCORES = {
  ")": 1, "]": 2, "}": 3, ">": 4
}

_KEYS = {
  "(": ")", ")": ")",
  "[": "]", "]": "]",
  "{": "}", "}": "}",
  "<": ">", ">": ">", 
}

# Actually we also need to track the last open, so let's just use a stack?

completion_scores = []
for i, line in enumerate(lines):
  stack = []
  line_score = 0
  discard = False
  for i, char in enumerate(line):
    if char in _OPEN:
      stack.append(char)
    else:
      if _KEYS[stack[-1]] != char:
        discard = True
        break
      else:
        stack.pop()
  if not discard:
    # evaluate score
    # print("Completion by ", stack)
    for char in stack[::-1]:
      line_score = 5 * line_score + _COMPLETION_SCORES[_KEYS[char]]
    completion_scores.append(line_score)

completion_scores.sort()
n = len(completion_scores)
# print(completion_scores)
ans = completion_scores[n // 2]
print(ans)