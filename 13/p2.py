import sys
from typing import Set, Tuple

assert len(sys.argv) > 1, "No input file given"
input_file_name = sys.argv[1]

lines = open(input_file_name).read().strip().split('\n')

ans = 0
max_x = 0
max_y = 0
points = set()
fold_instructions = []

for i, line in enumerate(lines):
  # filter out the middle empty line
  if not line:
    continue
  if line.startswith("fold"):
    fold, along, axis = line.split(' ')
    fold_instructions.append(axis)
  else:
    x, y = line.split(',')
    x, y = int(x), int(y)
    max_x = max(x, max_x)
    max_y = max(y, max_y)
    points.add((x, y))

# Complete the first fold instruction
def Fold(instruction: str, points: Set[Tuple[int]]) -> Set[Tuple[int]]:
  # print(f"Folding along {instruction}")
  direction, coord = instruction.split('=')
  coord = int(coord)
  points_to_add = set()
  points_to_remove = set()
  # fold vertically
  if direction == "x":
    for x, y in points:
      if x > coord:
        nx = 2 * coord - x
        points_to_add.add((nx, y))
        points_to_remove.add((x, y))
        # print(f"({x}, {y}) --> ({nx}, {y})")
  elif direction == "y":
    for x, y in points:
      if y > coord:
        ny = 2 * coord - y
        points_to_add.add((x, ny))
        points_to_remove.add((x, y))
        # print(f"({x}, {y}) --> ({x}, {ny})")
  else:
    print(f"Unknown folding instruction {instruction}")
  return points_to_add.union(points.difference(points_to_remove))

def Display(points: Set[Tuple[int]]) -> None:
  max_x = 0
  max_y = 0
  for x, y in points:
    max_x = max(x, max_x)
    max_y = max(y, max_y)
  width = max_x + 1
  height = max_y + 1
  grid = [["." for c in range(width)] for r in range(height)]
  for x, y in points:
    grid[y][x] = "#"
  print(" -------------------------- ")
  for row in grid:
    print(''.join(row))

for fold_instruction in fold_instructions:
  points = Fold(fold_instruction, points)
  Display(points)
