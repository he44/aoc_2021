import sys

assert len(sys.argv) > 1, "No input file given"
input_file_name = sys.argv[1]

lines = open(input_file_name).read().strip().split('\n')

count_nums = len(lines)
count_bits = len(lines[0])

one_counts = [0 for x in range(count_bits)]

for num_i in range(count_nums):
  for bit_i in range(count_bits):
    if lines[num_i][bit_i] == "1":
      one_counts[bit_i] += 1

gamma_rate = 0
epsilon_rate = 0

for i, one_count in enumerate(one_counts):
  exp = count_bits - 1 - i
  if one_count > count_nums // 2:
    gamma_rate += 2 ** exp
  else:
    epsilon_rate += 2 ** exp

ans = gamma_rate * epsilon_rate

print(ans)





