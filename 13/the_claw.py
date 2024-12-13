from util import assert_equals, file_to_array
INPUT = 'input.txt'
TEST_INPUT = 'test_input.txt'

class Game:
  x = 0
  y = 0
  a = (0, 0)
  b = (0, 0)

def min_buttons(file, offset=False):
  unparsed = file_to_array(file)
  rules = parse(unparsed, offset)
  total = 0
  for game in rules:
    total += solve(game)
  return total

def parse(unparsed, offset):
  rules = []
  current = Game()
  for row in unparsed:
    if row == "":
      rules.append(current)
      current = Game()
    elif "A" in row:
      current.a = get_params(row, "+")
    elif "B" in row:
      current.b = get_params(row, "+")
    else:
      x, y = get_params(row, "=")
      current.x = x + 10000000000000 if offset else x
      current.y = y + 10000000000000 if offset else y
  rules.append(current) # append final, oops
  return rules

def get_params(s, char):
  values = s.split(char)
  x = int(values[1].split(",")[0])
  y = int(values[2])
  return x, y

def solve(game):
  press_a = (game.x*game.b[1] - game.y*game.b[0]) / (game.a[0]*game.b[1] - game.a[1]*game.b[0])
  press_b = (game.y*game.a[0] - game.x*game.a[1]) / (game.a[0]*game.b[1] - game.a[1]*game.b[0])
  if press_a % 1 != 0 or press_b % 1 != 0:
    return 0
  return int(press_a * 3 + press_b)

assert_equals(min_buttons(TEST_INPUT), 480)
print("Part One: ", min_buttons(INPUT))
print("Part Two: ", min_buttons(INPUT, True))
