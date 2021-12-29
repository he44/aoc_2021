import sys
from typing import List, Tuple

assert len(sys.argv) > 1, "No input file given"
input_file_name = sys.argv[1]

lines = open(input_file_name).read().strip().split('\n')

ans = 0
grid = []
for i, line in enumerate(lines):
  grid.append([int(x) for x in line])

DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)]
def IsLowPoint(loc: Tuple[int]) -> bool:
  x, y = loc
  for dx, dy in DIRS:
    nx, ny = x + dx, y + dy
    cand = grid[nx][ny] if 0 <= nx < height and 0 <= ny < width else float('inf')
    if cand <= grid[x][y]:
      return False
  return True

ans = 0
height = len(grid)
width = len(grid[0])

for r in range(height):
  for c in range(width):
    if IsLowPoint((r, c)):
      print(r, c)
      ans += (1 + grid[r][c])

print(ans)