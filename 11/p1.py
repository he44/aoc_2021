from collections import deque
import sys
from typing import List

assert len(sys.argv) > 1, "No input file given"
input_file_name = sys.argv[1]

lines = open(input_file_name).read().strip().split('\n')

grid = []
for line in lines:
  grid.append([int(x) for x in line])

def SimulateOneStep(grid: List[List[int]]) -> int:
  height = len(grid)
  width = len(grid[0])
  queue = deque()
  flashed = set()
  # Increase Energy Level
  for r in range(height):
    for c in range(width):
      grid[r][c] += 1
      if grid[r][c] > 9:
        queue.append((r, c))
        flashed.add((r, c))
  # BFS
  while queue:
    cx, cy = queue.popleft()
    grid[cx][cy] = 0
    for dx in range(-1, 2):
      for dy in range(-1, 2):
        if dx == 0 and dy == 0:
          continue
        nx, ny = cx + dx, cy + dy
        if 0 <= nx < height and 0 <= ny < width and (nx, ny) not in flashed:
          grid[nx][ny] += 1
          if grid[nx][ny] > 9:
            queue.append((nx, ny))
            flashed.add((nx, ny))
  return len(flashed)

# print(grid)

_NUM_STEPS = 100
ans = 0

for _ in range(_NUM_STEPS):
  # print(" ------------------------------------------ ")
  # for row in grid:
  #   print(row)
  ans += SimulateOneStep(grid)
# print(" ------------------------------------------ ")
# for row in grid:
  # print(row)
print(ans)