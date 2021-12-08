import sys

assert len(sys.argv) > 1, "No input file given"
input_file_name = sys.argv[1]

# Minimizing L1 loss by finding the mode

lines = open(input_file_name).read().strip().split('\n')

nums = [int(x) for x in lines[0].split(',')]

last_pos = 0
largest_count = 0

counts = {}
for num in nums:
  counts[num] = counts.get(num, 0) + 1
  if counts[num] > largest_count:
    last_pos = num
    largest_count = counts[num]

ans1 = 0
ans = float('inf')


for x in counts:
  candidate = sum([abs(y - x) * counts[y] for y in counts])
  if ans > candidate:
    real_last_pos = x
    ans = candidate
  if x == last_pos:
    ans1 = ans
print(f"My wrong answer using mode moves to {last_pos} with cost {ans1}")
print(f"True answer using brute force moves to {real_last_pos} with cost {ans}")

