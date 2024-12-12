from util import assert_equals, file_to_array

INPUT = 'input.txt'
TEST_INPUT = 'test_input.txt'
TEST_INPUT_2 = 'test_input_2.txt'
TEST_INPUT_3 = 'test_input_3.txt'
DIRS = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def fence_cost(file):
  plots = file_to_array(file)
  regions = {}
  visited = set()
  cost = 0

  for y, row in enumerate(plots):
    for x, plot in enumerate(row):
      if (y, x) not in visited:
        p, a = build_region(y, x, visited, plot, plots)
        cost += p * a
  return cost

def build_region(y1, x1, visited, plot_type, plots):
  if (y1, x1) in visited:
    return 0, 0

  perimeter = 0
  area = 1
  visited.add((y1, x1))
  for direction in DIRS:
    y2, x2 = y1 + direction[1], x1 + direction[0]
    if not (0 <= y2 < len(plots)) or \
       not (0 <= x2 < len(plots[0])) or \
       plot_type != plots[y2][x2]:
      perimeter += 1
    else:
      p, a = build_region(y2, x2, visited, plot_type, plots)
      perimeter += p
      area += a

  return perimeter, area

assert_equals(fence_cost(TEST_INPUT), 140)
assert_equals(fence_cost(TEST_INPUT_2), 772)
assert_equals(fence_cost(TEST_INPUT_3), 1930)
print("Part One: ", fence_cost(INPUT))
