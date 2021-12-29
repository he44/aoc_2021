from collections import deque
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

queue = deque()
visited = set()
color = 0
for r in range(height):
  for c in range(width):
    if IsLowPoint((r, c)):
      queue.append((r, c, color))
      visited.add((r,c))
      color += 1

# Running BFS on starting from the low point?
# And we have to mark the color of each point?

# {color : count} there are |count| points that are within the basin marked
# by |color|.
sizes = [0 for x in range(color)]
dist = -1
while queue:
  cx, cy, color = queue.popleft()
  val = grid[cx][cy]
  sizes[color] += 1
  for dx, dy in DIRS:
    nx, ny = cx + dx, cy + dy
    if 0 <= nx < height and 0 <= ny < width and val < grid[nx][ny] < 9 and (nx, ny) not in visited:
      queue.append((nx, ny, color))
      visited.add((nx, ny))
sizes.sort(reverse=True)
ans = sizes[0] * sizes[1] * sizes[2]
print(sizes)
print(ans)

      
