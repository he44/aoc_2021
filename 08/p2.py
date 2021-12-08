import sys


_NUM_TO_DISPLAY = {
  0: "abcefg",
  1: "cf",
  2: "acdeg",
  3: "acdfg",
  4: "bcdf",
  5: "abdfg",
  6: "abdefg",
  7: "acf",
  8: "abcdefg",
  9: "abcdfg"
}

# We should count how many times each letter shows up from 1 - 10
counts = {x : 0 for x in "abcdefg"}
for num, display in _NUM_TO_DISPLAY.items():
  for char in display:
    counts[char] += 1

_COUNT_TO_LETTER = {}
for letter, count in counts.items():
  if count not in _COUNT_TO_LETTER:
    _COUNT_TO_LETTER[count] = []
  _COUNT_TO_LETTER[count].append(letter)


_MAGIC = 10
_UNIQUE_LENGTHS = {2: 1, 3: 7, 4: 4, 7: 8}
# length | number
# 2 | 1
# 3 | 7
# 4 | 4
# 7 | 8

_DISPLAY_TO_NUM = {val : key for (key,val) in _NUM_TO_DISPLAY.items()}

_LENGTH_TO_NUM = {}
for string, num in _DISPLAY_TO_NUM.items():
  size = len(string)
  if size not in _LENGTH_TO_NUM:
    _LENGTH_TO_NUM[size] = []
  _LENGTH_TO_NUM[size].append(num)


assert len(sys.argv) > 1, "No input file given"
input_file_name = sys.argv[1]

lines = open(input_file_name).read().strip().split('\n')

def solve_an_entry(input_vals: str, output_vals: str) -> int:
  input_strings = input_vals.split(' ')
  output_strings = output_vals.split(' ')
  assert len(input_strings) == _MAGIC, f"Wrong number of patterns, {input_strings}"

  # Stores mapping of new_segment to old_segment
  # "c" --> "a" menas "c" will turn on the top bar in this entry
  mapping = {}

  # We know the count in the original wiring
  # {8: ['a', 'c'], 6: ['b'], 7: ['d', 'g'], 4: ['e'], 9: ['f']}
  # we can tell b,e,f right away
  new_counts = {x : 0 for x in "abcdefg"}
  for pattern in input_strings:
    for char in pattern:
      new_counts[char] += 1
  for letter, count in new_counts.items():
    if count == 6:
      mapping[letter] = "b"
    elif count == 4:
      mapping[letter] = "e"
    elif count == 9:
      mapping[letter] = "f"

  # We know the length for each display 
  # {6: [0, 6, 9], 2: [1], 5: [2, 3, 5], 4: [4], 3: [7], 7: [8]
  # we can find display for 1, 4, 7, and 8 right away
  unique_size_nums = {1: None, 4: None, 7: None, 8: None}
  for pattern in input_strings:
    size = len(pattern)
    if size in _UNIQUE_LENGTHS:
      unique_size_nums[_UNIQUE_LENGTHS[size]] = pattern

  # we know originally 1 = "cf" and we know "f"
  # --> we know "c"
  for letter in unique_size_nums[1]:
    if letter not in mapping:
      mapping[letter] = "c"
  
  # we know originally 7 = "acf" and we know "f", "c"
  # --> we know "a"
  for letter in unique_size_nums[7]:
    if letter not in mapping:
      mapping[letter] = "a"

  # we know originally 4 = "bcdf", and we know "b", c", "f"
  # --> we know "d"
  for letter in unique_size_nums[4]:
    if letter not in mapping:
      mapping[letter] = "d"

  # the last one will be "g"
  for letter in "abcdefg":
    if letter not in mapping:
      mapping[letter] = "g"

  # compute output values
  this_num = 0
  for pattern in output_strings:
    original_wiring = ''.join(sorted([mapping[x] for x in pattern]))
    value = _DISPLAY_TO_NUM[original_wiring]
    this_num = this_num * 10 + value

  return this_num

ans = 0
for i, line in enumerate(lines):
  input_values, output_values = line.split(" | ")
  ans += solve_an_entry(input_values, output_values)

print(ans)


