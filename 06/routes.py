from copy import deepcopy

from util import assert_equals, file_to_array

INPUT = 'input.txt'
TEST_INPUT = 'test_input.txt'

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
  room = [list(row) for row in file_to_array(file)]
  total = 0
  coords = (0,0) # y, x
  for y, row in enumerate(room):
    if "^" in row:
      x = row.index("^")
      coords = (y, x)
      break

  for y, row in enumerate(room):
    for x, cell in enumerate(row):
      if cell != ".":
        continue
      room_clone = deepcopy(room)
      room_clone[y][x] = "#"
      total += find_loop(room_clone, coords)

  return total

def find_loop(room, start):
  coords = start
  orientation = (-1,0)
  traveled = {(coords[0], coords[1], orientation[0], orientation[1])}
  while True:
    next = (coords[0] + orientation[0], coords[1] + orientation[1])
    if not (0 <= next[0] < len(room) and 0 <= next[1] < len(room[0])):
      return 0
    if room[next[0]][next[1]] == "#":
      orientation = (orientation[1], orientation[0] * -1)
      continue
    coords = next
    node = (coords[0], coords[1], orientation[0], orientation[1])
    if node in traveled:
      return 1
    traveled.add(node)

assert_equals(total_positions(TEST_INPUT), 41)
print("Part One: ", total_positions(INPUT))
assert_equals(total_loops(TEST_INPUT), 6)
print("Part Two: ", total_loops(INPUT))