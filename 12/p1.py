import sys
from typing import List

assert len(sys.argv) > 1, "No input file given"
input_file_name = sys.argv[1]

lines = open(input_file_name).read().strip().split('\n')

graph = {}

unvisited = set()
for line in lines:
  src, dst = line.split('-')
  if src not in graph:
    graph[src] = set()
  graph[src].add(dst)
  if dst not in graph:
    graph[dst] = set()
  graph[dst].add(src)
  if src[0].islower():
    unvisited.add(src)
  if dst[0].islower():
    unvisited.add(dst)

print(graph)

# backtrack + memoization?
ans = 0

def dfs(cur_node: str, cur_path: List[str]) -> None:
  # print(cur_node)
  if cur_node == "end":
    print(cur_path)
    return 1
  num = 0
  for neighbor in graph[cur_node]:
    removed = False
    if neighbor == "start":
      continue
    if neighbor[0].islower():
      if neighbor not in unvisited:
        continue
      unvisited.remove(neighbor)
      removed = True
    cur_path.append(neighbor)
    num += dfs(neighbor, cur_path)
    cur_path.pop()
    if removed:
      unvisited.add(neighbor)
  return num

ans = dfs("start", ["start"])

print(ans)