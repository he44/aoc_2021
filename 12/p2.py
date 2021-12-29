import sys
from typing import List

assert len(sys.argv) > 1, "No input file given"
input_file_name = sys.argv[1]

lines = open(input_file_name).read().strip().split('\n')

graph = {}

for line in lines:
  src, dst = line.split('-')
  if src not in graph:
    graph[src] = set()
  graph[src].add(dst)
  if dst not in graph:
    graph[dst] = set()
  graph[dst].add(src)

print(graph)

# backtrack + memoization?
ans = 0

visited = set()
def dfs(cur_node: str, cur_path: List[str], twice: bool) -> None:
  # print(cur_node)
  if cur_node == "end":
    print(cur_path)
    return 1
  num = 0
  for neighbor in graph[cur_node]:
    if neighbor == "start":
      continue
    if neighbor[0].isupper() or neighbor == "end":
      cur_path.append(neighbor)
      num += dfs(neighbor, cur_path, twice)
      cur_path.pop()
    else:
      if neighbor in visited and twice:
        continue
      if neighbor in visited:
        twice = True
        cur_path.append(neighbor)
        num += dfs(neighbor, cur_path, twice)
        cur_path.pop()
        twice = False
      else:
        visited.add(neighbor)
        cur_path.append(neighbor)
        num += dfs(neighbor, cur_path, twice)
        cur_path.pop()
        visited.remove(neighbor)
  return num

ans = dfs("start", ["start"], False)

print(ans)