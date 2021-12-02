_INPUT_NAME = "e1.txt"
_INPUT_NAME = "i1.txt"

lines = open(_INPUT_NAME).read().strip().split('\n')

ans = 0
horizontal_pos = 0
vertical_pos = 0
aim = 0
for command in lines:
  direction, distance = command.split(" ")
  distance = int(distance)
  if direction == "forward":
    horizontal_pos += distance
    vertical_pos += aim * distance
  elif direction == "up":
    aim -= distance
  elif direction == "down":
    aim += distance
  else:
    print(f"Something went wrong, {direction}")
print(horizontal_pos * vertical_pos)



