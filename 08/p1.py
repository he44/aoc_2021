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

_UNIQUE_LENGTHS = {2, 3, 4, 7}

_DISPLAY_TO_NUM = {val : key for (key,val) in _NUM_TO_DISPLAY.items()}

_LENGTH_TO_NUM = {}
for string, num in _DISPLAY_TO_NUM.items():
  size = len(string)
  if size not in _LENGTH_TO_NUM:
    _LENGTH_TO_NUM[size] = []
  _LENGTH_TO_NUM[size].append(num)

print(_NUM_TO_DISPLAY)
print(_DISPLAY_TO_NUM)
print(_LENGTH_TO_NUM)

assert len(sys.argv) > 1, "No input file given"
input_file_name = sys.argv[1]

lines = open(input_file_name).read().strip().split('\n')

ans = 0
for i, line in enumerate(lines):
  input_values, output_values = line.split(" | ")
  for output_val in output_values.split(" "):
    if len(output_val) in _UNIQUE_LENGTHS:
      ans += 1

print(ans)


