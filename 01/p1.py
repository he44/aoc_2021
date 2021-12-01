_INPUT_NAME = "i1.txt"

lines = open(_INPUT_NAME).read().strip().split('\n')

ans = 0
for i, line in enumerate(lines[1:], 1):
  depth = int(line)
  if depth > int(lines[i-1]):
    ans += 1
print(ans)



