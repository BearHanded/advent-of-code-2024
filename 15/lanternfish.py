from util import assert_equals, file_to_subarray

INPUT = 'input.txt'
TEST_INPUT = 'test_input.txt'
TEST_INPUT_2 = 'test_input_2.txt'
MOVES = {
  "^": (-1, 0),
  "v": (1, 0),
  "<": (0, -1),
  ">": (0, 1),
}

def simulate(file):
  chunked = file_to_subarray(file)
  warehouse = [list(row) for row in chunked[0]]
  moves = "".join(chunked[1])

  # find character
  y, x = 0, 0
  for cy, row in enumerate(warehouse):
    for cx, cell in enumerate(row):
      if cell == "@":
        y, x = cy, cx
        warehouse[y][x] = "."
        break
  # run
  for move in moves:
    y, x = attempt_move(move, y, x, warehouse)

  return sum_gps(warehouse)

def sum_gps(warehouse):
  # 100 * distance from top + distance from left
  total = 0
  for y, row in enumerate(warehouse):
    for x, cell in enumerate(row):
      if cell == "O":
        total += 100*y + x
  return total

def attempt_move(move, y, x, warehouse):
  vector = MOVES[move]
  next_y = y + vector[0]
  next_x = x + vector[1]
  if warehouse[next_y][next_x] == ".":
    return next_y, next_x
  elif warehouse[next_y][next_x] == "#":
    return y, x

  # pushing box
  next_box_y = next_y + vector[0]
  next_box_x = next_x + vector[1]
  while True:
    if warehouse[next_box_y][next_box_x] == "#": # can't push into wall
      return y, x
    if warehouse[next_box_y][next_box_x] == ".": # push stack
      warehouse[next_y][next_x] = "."
      warehouse[next_box_y][next_box_x] = "O"
      return next_y, next_x
    # found another box, keep going
    next_box_y += vector[0]
    next_box_x += vector[1]


assert_equals(simulate(TEST_INPUT_2), 2028)
assert_equals(simulate(TEST_INPUT), 10092)
print("Part One: ", simulate(INPUT))
