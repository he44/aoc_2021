import sys

assert len(sys.argv) > 1, "No input file given"
input_file_name = sys.argv[1]

lines = open(input_file_name).read().strip().split('\n')

count_nums = len(lines)
count_bits = len(lines[0])

# Generating the number of 1s at each bit position.
one_counts = [0 for x in range(count_bits)]
for num_i in range(count_nums):
  for bit_i in range(count_bits):
    if lines[num_i][bit_i] == "1":
      one_counts[bit_i] += 1

# Checking bit by bit
# most common
oxy_counts = one_counts[:]
discarded_oxy_indices = set()
skip_oxy = False
# least common
co2_counts = one_counts[:]
discarded_co2_indices = set()
skip_co2 = False

# Going through bit position one by one.
for bit_i in range(count_bits):
  skip_oxy = (len(discarded_oxy_indices) == count_nums - 1)
  skip_co2 = (len(discarded_co2_indices) == count_nums - 1)
  remain_oxy_counts = count_nums - len(discarded_oxy_indices)
  remain_co2_counts = count_nums - len(discarded_co2_indices)
  oxy_common_bit = "1" if oxy_counts[bit_i] >= remain_oxy_counts - oxy_counts[bit_i] else "0"
  co2_common_bit = "1" if co2_counts[bit_i] >= remain_co2_counts - co2_counts[bit_i] else "0"
  # Going through numbers one by one.
  for num_i, num in enumerate(lines):
    bit = num[bit_i]
    # For remaining oxy number that doesnot have common bit
    if not skip_oxy and num_i not in discarded_oxy_indices and bit != oxy_common_bit:
      # Discard this number
      discarded_oxy_indices.add(num_i)
      # Update the count
      for i in range(count_bits):
        if num[i] == "1":
          oxy_counts[i] -= 1
    # Same thing for CO2
    if not skip_co2 and num_i not in discarded_co2_indices and bit == co2_common_bit:
      discarded_co2_indices.add(num_i)
      for i in range(count_bits):
        if num[i] == "1":
          co2_counts[i] -= 1

oxy_rating = 0
co2_rating = 0
for num_i, num in enumerate(lines):
  if num_i not in discarded_oxy_indices:
    oxy_rating = int(num, 2)
  if num_i not in discarded_co2_indices:
    co2_rating = int(num, 2)
ans = oxy_rating * co2_rating
print(ans)



