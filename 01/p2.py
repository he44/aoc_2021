_INPUT_NAME = "i2.txt"
_WINDOW_SIZE = 3

lines = open(_INPUT_NAME).read().strip().split('\n')
depths = [int(x) for x in lines]

n = len(depths)
cur_window_sum = sum(depths[:_WINDOW_SIZE])
prev_window_sum = cur_window_sum

ans = 0
for window_i in range(1, n - _WINDOW_SIZE + 1):
  prev_window_sum = cur_window_sum
  cur_window_sum -= depths[window_i - 1]
  cur_window_sum += depths[window_i + _WINDOW_SIZE - 1]
  if cur_window_sum > prev_window_sum:
    ans += 1
print(ans)




