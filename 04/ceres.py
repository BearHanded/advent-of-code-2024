from util import assert_equals, file_to_array

INPUT = '04/input.txt'
TEST_INPUT = '04/test_input.txt'
TEST_INPUT_2 = '04/test_input2.txt'


DIRS = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]
MATCH = "XMAS"
PATTERN = ["M.S", \
           ".A.", \
           "M.S"]
PATTERNS = [PATTERN]
PATTERNS.append(list(zip(*PATTERNS[-1][::-1])))
PATTERNS.append(list(zip(*PATTERNS[-1][::-1])))
PATTERNS.append(list(zip(*PATTERNS[-1][::-1])))

# Part One
def total_xmas(file):
  total = 0
  puzzle = file_to_array(file)
  
  for y, row in enumerate(puzzle):
    for x, char in enumerate(row):
      if char == "X":
        total += find_xmas(puzzle, x, y)
  return total

def find_xmas(puzzle, x, y):
  matches = 0
  for dir in DIRS:
    if (
        0 <= x + dir[0] * 3 < len(puzzle[0]) and
        0 <= y + dir[1] * 3 < len(puzzle) and
        puzzle[y][x] + puzzle[y+dir[1]][x+dir[0]] + puzzle[y+dir[1]*2][x+dir[0]*2] + puzzle[y+dir[1]*3][x+dir[0]*3] == "XMAS"
       ):
      matches += 1
  return matches

# Part Two
def total_pattern(file):
  total = 0
  puzzle = file_to_array(file)
  
  for y in range(len(puzzle)-2):
    for x in range(len(puzzle[0])-2):
        total += find_pattern(puzzle, x, y)
  return total

def find_pattern(puzzle, x, y):
  for rotation in PATTERNS:
    valid = True
    for yp in range(3):
      for xp in range(3):
        if rotation[yp][xp] == ".":
          continue
        if rotation[yp][xp] != puzzle[y+yp][x+xp]:
          valid = False
          break
      if not valid:
        break
    if valid:
      return 1
  return 0

assert_equals(total_xmas(TEST_INPUT), 4)
assert_equals(total_xmas(TEST_INPUT_2), 18)
print("Part One: ", total_xmas(INPUT))
assert_equals(total_pattern(TEST_INPUT_2), 9)
print("Part Two: ", total_pattern(INPUT))