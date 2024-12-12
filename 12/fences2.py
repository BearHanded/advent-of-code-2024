from util import assert_equals, file_to_array

INPUT = 'input.txt'
TEST_INPUT = 'test_input.txt'
TEST_INPUT_2 = 'test_input_2.txt'
TEST_INPUT_3 = 'test_input_3.txt'
DIRS = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def fence_cost(file):
  plots = file_to_array(file)
  visited = set()
  cost = 0

  for y, row in enumerate(plots):
    for x, plot in enumerate(row):
      if (y, x) not in visited:
        region = build_region(y, x, set(), plot, plots) # isolate shape
        sides = count_sides(region, len(plots), len(plots[0]))
        cost += sides * len(region)
        visited = visited.union(region)
  return cost

def build_region(y1, x1, region, plot_type, plots):
  if (y1, x1) in region:
    return region
  region.add((y1, x1))
  for direction in DIRS:
    y2, x2 = y1 + direction[1], x1 + direction[0]
    if 0 <= y2 < len(plots) and \
       0 <= x2 < len(plots[0]) and \
       plot_type == plots[y2][x2]:
      region.union(build_region(y2, x2, region, plot_type, plots))
  return region

def count_sides(region, max_y, max_x):
  sides = 0

  side_right, side_down, side_left, side_up = False, False, False, False

  # V sides
  for x in range(-1, max_x+1):
    for y in range(-1, max_y+1):
      if (y, x) not in region and (y, x+1) in region:
        if not side_right:
          sides += 1
          side_right = True
      else:
        side_right = False

      if (y, x) not in region and (y, x-1) in region:
        if not side_left:
          sides += 1
          side_left = True
      else:
        side_left = False

  # H Sides
  for y in range(-1, max_y+1):
    for x in range(-1, max_x+1):
      if (y, x) not in region and (y+1, x) in region:
        if not side_down:
          sides += 1
          side_down = True
      else:
        side_down = False

      if (y, x) not in region and (y-1, x) in region:
        if not side_up:
          sides += 1
          side_up = True
      else:
        side_up = False
  return sides

assert_equals(fence_cost(TEST_INPUT), 80)
assert_equals(fence_cost(TEST_INPUT_2), 436)
assert_equals(fence_cost(TEST_INPUT_3), 1206)
print("Part Two: ", fence_cost(INPUT))
