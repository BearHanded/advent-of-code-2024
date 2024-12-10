from util import assert_equals, file_as_string, file_to_array

INPUT = 'input.txt'
TEST_INPUT = 'test_input.txt'
TEST_INPUT_2 = 'test_input_2.txt'
DIRS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
visited = {}

def total_score(file, rating=False):
  topology = [[int(i) for i in row] for row in file_to_array(file)]
  score = 0

  for y, row in enumerate(topology):
    for x, cell in enumerate(row):
      if cell == 0:
        if not rating:
          score += len(get_score(topology, y, x))
        else:
          score += get_rating(topology, y, x)
  return score

def get_score(topology, y, x):
  peaks = set()
  for direction in DIRS:
    x1 = x + direction[1]
    y1 = y + direction[0]
    if 0 <= x1 < len(topology[0]) and \
       0 <= y1 < len(topology[1]) and \
       topology[y1][x1] == topology[y][x] + 1:
      if topology[y1][x1] == 9:
        peaks.add((y1, x1))
      else:
        peaks = peaks.union(get_score(topology, y1, x1))
  return peaks

def get_rating(topology, y, x):
  score = 0
  for direction in DIRS:
    x1 = x + direction[1]
    y1 = y + direction[0]
    if 0 <= x1 < len(topology[0]) and \
       0 <= y1 < len(topology[1]) and \
       topology[y1][x1] == topology[y][x] + 1:
      if topology[y1][x1] == 9:
        score += 1
      else:
        score += get_rating(topology, y1, x1)
  return score


assert_equals(total_score(TEST_INPUT), 1)
assert_equals(total_score(TEST_INPUT_2), 36)
print("Part One: ", total_score(INPUT))
assert_equals(total_score(TEST_INPUT_2, rating=True), 81)
print("Part Two: ", total_score(INPUT, rating=True))