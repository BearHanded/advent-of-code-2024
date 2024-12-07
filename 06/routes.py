from util import assert_equals, file_to_array

INPUT = '06/input.txt'
TEST_INPUT = '06/test_input.txt'

def total_positions(file):
  room = file_to_array(file)
  coords = (0,0) # y, x
  orientation = (-1,0) # y, x
  for y, row in enumerate(room):
    if "^" in row:
      x = row.index("^")
      coords = (y, x)
      break
  traveled = {(y,x)}
  
  # walk
  while True:
    next = (coords[0] + orientation[0], coords[1] + orientation[1])
    if not (0 <= next[0] < len(room) and 0 <= next[1] < len(room[0])):
      break
    if room[next[0]][next[1]] == "#":
      orientation = (orientation[1], orientation[0] *-1)
      continue
    coords = next
    traveled.add(coords)

  return len(traveled)
  

def total_loops(file):
  room = file_to_array(file)
  coords = (0,0) # y, x
  orientation = (-1,0) # y, x
  for y, row in enumerate(room):
    if "^" in row:
      x = row.index("^")
      coords = (y, x)
      break
  traveled = {}
  

  for y, row in enumerate(room):
    for x, cell in enumerate(row):
      if cell != ".":
        continue
      # deep copy room
      # replace . with #
      # test walk for loop
      while True:
        traveled.add(coords)
        next = (coords[0] + orientation[0], coords[1] + orientation[1])
        if not (0 <= next[0] < len(room) and 0 <= next[1] < len(room[0])):
          break
        if room[next[0]][next[1]] == "#":
          orientation = (orientation[1], orientation[0] *-1)
          continue
        coords = next




assert_equals(total_positions(TEST_INPUT), 41)
print("Part One: ", total_positions(INPUT))
assert_equals(total_loops(TEST_INPUT), 4)
print("Part Two: ", total_loops(INPUT))