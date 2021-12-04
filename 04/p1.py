import sys
from typing import List, Set

assert len(sys.argv) > 1, "No input file given"
input_file_name = sys.argv[1]

lines = open(input_file_name).read().strip().split('\n\n')

num_pool = lines[0]
raw_boards = lines[1:]

# Pre-process inputs
num_pool = [int(x) for x in num_pool.split(',')]

boards = []
for raw_board in raw_boards:
  # one/two spaces both handled using default parameter
  raw_rows = raw_board.split('\n') 
  board = []
  for row in raw_rows:
    board.append([int(x) for x in row.split()])
  boards.append(board)

def wins(board: List[List[int]]) -> bool:
  n = len(board)
  assert n == 5 and len(board[0]) == 5, f"Wrong dimension {n} * {len(board[0])}"
  for row in board:
    if sum(row) == n:
      return True
  for c in range(n):
    # This is not numpy, sum(board[:][c]) won't work
    # I think it will still return the row sum?
    col = [board[r][c] for r in range(n)]
    if sum(col) == n:
      return True
  return False

def mark(board: List[List[int]], pool: Set[int]) -> List[List[int]]:
  n = len(board)
  assert n == 5 and len(board[0]) == 5, f"Wrong dimension {n} * {len(board[0])}"
  markers = [[0 for c in range(n)] for r in range(n)]
  for r in range(n):
    for c in range(n):
      if board[r][c] in pool:
        markers[r][c] = 1
  return markers


ans = 0
found_winner = False
pool_set = set()
for num in num_pool:
  pool_set.add(num)
  # Mark and check for winners
  for i, board in enumerate(boards):
    selection_board = mark(board, pool_set)
    if wins(selection_board):
      found_winner = True
      break
  if found_winner:
    break

print(f"Winning number is {num}")
print(f"Winning board is \n {board}")
print(f"Winning board selection is \n {selection_board}")

n = len(board)
for r in range(n):
  for c in range(n):
    ans += (1 - selection_board[r][c]) * board[r][c]
ans *= num

print(ans)


