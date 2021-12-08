import sys

assert len(sys.argv) > 1, "No input file given"
input_file_name = sys.argv[1]

lines = open(input_file_name).read().strip().split('\n')

ans = 0
counts = {}
for i, line in enumerate(lines):
  start, end = line.split(' -> ')
  x1, y1 = start.split(',')
  x2, y2 = end.split(',')
  x1 = int(x1)
  y1 = int(y1)
  x2 = int(x2)
  y2 = int(y2)
  # Diagonal going southeast
  if (y1 - x1 == y2 - x2):
    for r in range(min(x1, x2), max(x1, x2) + 1):
      c = y1 - x1 + r
      counts[(r, c)] = counts.get((r, c), 0) + 1
  # Diagonal going northeast
  elif (x1 + y1 == x2 + y2):
    for r in range(min(x1, x2), max(x1, x2) + 1):
      counts[(r, x1 + y1 - r)] = counts.get((r, x1 + y1 - r), 0) + 1
  elif x1 == x2:
    for c in range(min(y1, y2), max(y1, y2) + 1):
      counts[(x1, c)] = counts.get((x1, c), 0) + 1
  elif y1 == y2:
    for r in range(min(x1, x2), max(x1, x2) + 1):
      counts[(r, y1)] = counts.get((r, y1), 0) + 1
for point in counts:
  if counts[point] >= 2:
    ans += 1


print(ans)


