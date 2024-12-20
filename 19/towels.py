from functools import cache
from util import assert_equals, file_to_subarray

INPUT = 'input.txt'
TEST_INPUT = 'test_input.txt'

def count_valid(file, every_combo):
  towels, orders = file_to_subarray(file)
  towels = tuple(towels[0].split(", "))

  total = 0
  for order in orders:
    if every_combo: # P2
      total += total_valid_options(order, towels)
    else: #P1
      total += order_valid(order, towels)
  return total

@cache
def order_valid(order, towels):
  for towel in towels:
    if order.startswith(towel):
      if towel == order:
        return 1
      else:
        valid = order_valid(order[len(towel):], towels)
        if valid:
          return 1
  return 0

@cache
def total_valid_options(order, towels):
  total = 0
  for towel in towels:
    if towel == order:
      total += 1
    elif order.startswith(towel):
      total += total_valid_options(order[len(towel):], towels)
  return total

assert_equals(count_valid(TEST_INPUT, False), 6)
print("Part One: ", count_valid(INPUT, False))
assert_equals(count_valid(TEST_INPUT, True), 16)
print("Part Two: ", count_valid(INPUT, True))
