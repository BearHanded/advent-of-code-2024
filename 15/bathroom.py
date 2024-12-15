import re

from util import assert_equals, file_to_array
INPUT = 'input.txt'
TEST_INPUT = 'test_input.txt'

class Bot:
  vx = 0
  vy = 0
  x = 0
  y = 0

  def __init__(self, x, y, vx, vy):
    self.x = x
    self.y = y
    self.vx = vx
    self.vy = vy

def bathroom_bots(file, width, height, t, pretty=False):
  bots = parse(file)
  elapse(bots, width, height, t, pretty, t)
  return count_quadrants(bots, width, height)

def run_bots(file, width, height, time_start, time_end):
  bots = parse(file)
  for t in range(time_start, time_end):
    elapse(bots, width, height, 1, True, t)

def parse(file):
  unparsed = file_to_array(file)
  bots = []
  for row in unparsed:
    px, py, vx, vy = list(map(int, re.findall(r'[+-]?\d+(?:\.\d+)?', row)))
    bot = Bot(px, py, vx, vy)
    bots.append(bot)

  return bots

def elapse(bots, w, h, step, pretty, pretty_time):
  display = [[0] * w for i in range(h)]
  for bot in bots:
    bot.x = (bot.x + bot.vx * step) % w
    bot.y = (bot.y + bot.vy * step) % h

    display[bot.y][bot.x] += 1

  if not pretty:
    return

  suspicious = False
  pixels = []

  for r in display:
    pixel_row = ''.join(["◼" if c else " " for c in r])
    if "◼◼◼◼◼◼◼" in pixel_row:
      suspicious = True
    pixels.append(pixel_row)
  if not suspicious:
    return

  print("\n")
  print("BOTS AT TIME:", pretty_time)
  for r in pixels:
    print(r)

def count_quadrants(bots, w, h):
  half_x = (w - 1) // 2
  half_y = (h - 1) // 2
  totals = [[0, 0], [0, 0]]
  for bot in bots:
    if bot.x == half_x or bot.y == half_y:
      continue
    qx = int(bot.x > half_x)
    qy = int(bot.y > half_y)
    totals[qx][qy] += 1
  return totals[0][0] * totals[0][1] * totals[1][0] * totals[1][1]



assert_equals(bathroom_bots(TEST_INPUT, 11, 7, 100), 12)
print("Part One: ", bathroom_bots(INPUT, 101, 103, 100))
print("Part Two: ", run_bots(INPUT, 101, 103, 1, 100000000))
