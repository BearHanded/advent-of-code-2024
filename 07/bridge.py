from copy import deepcopy

from util import assert_equals, file_to_array

INPUT = 'input.txt'
TEST_INPUT = 'test_input.txt'
OPERATIONS = [lambda x, y: x * y, lambda x, y: x + y, ]
concat_fn = lambda x, y : int(str(x) + str(y))

def sum_calibration(file, concat=False):
  total = 0
  equations = file_to_array(file)
  operations = OPERATIONS
  if concat:
    operations.append(concat_fn)

  for equation in equations:
    segments = equation.split(': ')
    target = int(segments[0])
    operands = [int(x) for x in segments[1].split(' ')]
    if test_operators(target, operands, operations):
      total += target
  return total

def test_operators(target, operands, operations):
  for operation in operations:
    result = operation(operands[0], operands[1])

    if result == target and len(operands) == 2:
      return True
    elif result <= target and len(operands) > 2:
      remaining = operands[2:]
      remaining.insert(0, result)
      if test_operators(target, remaining, operations):
        return True

  return False

assert_equals(sum_calibration(TEST_INPUT), 3749)
print("Part One: ", sum_calibration(INPUT))
assert_equals(concat_fn(123, 45), 12345)
assert_equals(sum_calibration(TEST_INPUT, concat=True), 11387)
print("Part Two: ", sum_calibration(INPUT))