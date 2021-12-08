import sys
import math

assert len(sys.argv) > 1, "No input file given"
input_file_name = sys.argv[1]



def compute_cost(final_pos: int, counts: dict) -> int:
  cost = 0
  for x in counts:
    dist = abs(final_pos - x)
    if dist != 0:
      cost += (dist * (dist + 1) // 2)* counts[x]
  return cost


lines = open(input_file_name).read().strip().split('\n')

nums = [int(x) for x in lines[0].split(',')]

counts = {}
for num in nums:
  counts[num] = counts.get(num, 0) + 1

ans = float('inf')
for x in counts:
  candidate = compute_cost(x, counts)
  if ans > candidate:
    real_last_pos = x
    ans = candidate
print(f"True answer using brute force moves to {real_last_pos} with cost {ans}")

# If using average, 457.xxx 
avg = sum(nums) / len(nums)
pos1 = int(math.floor(avg))
c1 = compute_cost(pos1, counts)
pos2 = int(math.ceil(avg))
c2 = compute_cost(pos2, counts)
print(f"Average is {avg}")
print(f"Using avg, we got {pos1} --> {c1} and {pos2} --> {c2}")

for i in range(17):
  counts = {i: 1}
  print(i, compute_cost(5, counts))
