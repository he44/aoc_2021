_INPUT_NAME = "i1.txt"

lines = open(_INPUT_NAME).read().strip().split('\n')

ans = 0
horizontal_pos = 0
vertical_pos = 0
for command in lines:
  direction, distance = command.split(" ")
  distance = int(distance)
  if direction == "forward":
    horizontal_pos += distance
  elif direction == "up":
    vertical_pos -= distance
  elif direction == "down":
    vertical_pos += distance
  else:
    print(f"Something went wrong, {direction}")
print(horizontal_pos * vertical_pos)



