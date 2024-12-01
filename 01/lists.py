from util import assert_equals, file_to_array

INPUT = '01/input.txt'
TEST_INPUT = '01/test_input.txt'

def distance_check(file):
  total = 0
  nums = [[int(num) for num in row.split("   ")] for row in file_to_array(file)]
  ordered = [sorted(row) for row in list(zip(*nums[::1]))]

  for idx, left in enumerate(ordered[0]):
    total += abs(left - ordered[1][idx])
  return total

def similarity_score(file):
  total = 0
  nums = [[int(num) for num in row.split("   ")] for row in file_to_array(file)]
  ordered = [sorted(row) for row in list(zip(*nums[::1]))]

  # find count in right list, += left * right
  for left in ordered[0]:
    total += left * ordered[1].count(left)
  return total

assert_equals(distance_check(TEST_INPUT), 11)
print("Part One: ", distance_check(INPUT))


assert_equals(similarity_score(TEST_INPUT), 31)
print("Part Two: ", similarity_score(INPUT))