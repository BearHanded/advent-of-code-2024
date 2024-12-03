from util import assert_equals, file_to_array

INPUT = '02/input.txt'
TEST_INPUT = '02/test_input.txt'

def row_safe(row, tolerant):
  valid = True
  row_diff = None
  for idx in range(len(row) - 1):
    diff = row[idx] - row[idx+1]
    if idx == 0:
      row_diff = diff
    if (diff * row_diff < 0) or not (1 <= abs(diff) <= 3):
      if not tolerant:
        valid = False
        break
      for pop_idx in range(len(row)):
        new_row = row.copy()
        new_row.pop(pop_idx)
        if row_safe(new_row, False):
          return True
      return False
  return valid
  

def total_safe(file, tolerant):
  total = 0
  nums = [[int(num) for num in row.split(" ")] for row in file_to_array(file)]
  for row in nums:
    if row_safe(row, tolerant):
      total += 1
  return total

assert_equals(total_safe(TEST_INPUT, False), 2)
print("Part One: ", total_safe(INPUT, False))
assert_equals(total_safe(TEST_INPUT, True), 4)
print("Part Two: ", total_safe(INPUT, True))