import copy

from util import assert_equals, file_to_subarray

INPUT = 'input.txt'
TEST_INPUT = 'test_input.txt'
TEST_INPUT_2 = 'test_input_2.txt'
TEST_INPUT_3 = 'test_input_3.txt'
MOVES = {
  "^": (-1, 0),
  "v": (1, 0),
  "<": (0, -1),
  ">": (0, 1),
}

def simulate(file):
  chunked = file_to_subarray(file)
  warehouse = [list(row) for row in chunked[0]]
  warehouse = expand(warehouse)
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
    y, x, new_warehouse = attempt_move(move, y, x, warehouse)
    warehouse = new_warehouse
  return sum_gps(warehouse)

def expand(warehouse):
  replacements = {
    "@": ["@", "."],
    "#": ["#", "#"],
    ".": [".", "."],
    "O": ["[", "]"]
  }
  new_warehouse = []
  for row in warehouse:
    new_row = []
    for c in row:
      new_row.extend(replacements[c])
    new_warehouse.append(new_row)
  return new_warehouse

def sum_gps(warehouse):
  total = 0
  for y, row in enumerate(warehouse):
    for x, cell in enumerate(row):
      if cell == "[":
        total += 100*y + x
  return total

def attempt_move(move, y, x, warehouse):
  vector = MOVES[move]
  next_y = y + vector[0]
  next_x = x + vector[1]
  if warehouse[next_y][next_x] == ".":
    return next_y, next_x, warehouse
  elif warehouse[next_y][next_x] == "#":
    return y, x, warehouse

  # pushing box
  valid, affected = check_push(vector, next_y, next_x, warehouse)
  if valid:
    new_warehouse = commit_push(vector, affected, warehouse)
    warehouse[next_y][next_x] = "." # pushed
    return next_y, next_x, new_warehouse # moved
  return y, x, warehouse



def check_push(vector, box_y, box_x, warehouse):
  box_cells = [(box_y, box_x)]
  other_half_offset = 1 if warehouse[box_y][box_x] == "[" else -1
  box_cells.append((box_y, box_x + other_half_offset))
  affected = set(box_cells)

  for voxel in box_cells:
    next_voxel_y = voxel[0] + vector[0]
    next_voxel_x = voxel[1] + vector[1]
    if (next_voxel_y, next_voxel_x) in box_cells or \
        warehouse[next_voxel_y][next_voxel_x] == ".":
      continue
    if warehouse[next_voxel_y][next_voxel_x] == "#":
      return False, affected
    valid_cell, affected_cells = check_push(vector, next_voxel_y, next_voxel_x, warehouse)
    if not valid_cell:
      return False, affected
    affected.update(affected_cells)

  return True, affected

def commit_push(vector, affected, warehouse):
  new_warehouse = copy.deepcopy(warehouse)
  for cell in affected: # draw empty where they left to handle unfilled locations
    new_warehouse[cell[0]][cell[1]] = "."

  for cell in affected: # draw new locations
    new_warehouse[cell[0] + vector[0]][cell[1] + vector[1]] = warehouse[cell[0]][cell[1]]
  return new_warehouse


assert_equals(simulate(TEST_INPUT_3), 105 + 207 + 306)
assert_equals(simulate(TEST_INPUT), 9021)
print("Part Two: ", simulate(INPUT))

