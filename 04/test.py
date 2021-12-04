from typing import List, Set

selection_board = [
  [0, 0, 1, 1, 0], 
  [1, 0, 1, 1, 1], 
  [0, 0, 1, 0, 1], 
  [0, 1, 1, 1, 1], 
  [1, 1, 1, 0, 0]
]

print(selection_board)

def wins(board: List[List[int]]) -> bool:
  n = len(board)
  assert n == 5 and len(board[0]) == 5, f"Wrong dimension {n} * {len(board[0])}"
  for row in board:
    if sum(row) == n:
      return True
  for c in range(n):
    # This is not numpy, sum(board[:][c]) won't work
    col = [board[r][c] for r in range(n)]
    if sum(col) == n:
      return True
  return False

print(wins(selection_board))
