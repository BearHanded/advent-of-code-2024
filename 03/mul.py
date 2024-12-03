from util import assert_equals, file_to_array
import re 

INPUT = '03/input.txt'
TEST_INPUT = '03/test_input.txt'
TEST_INPUT_2 = '03/test_input2.txt'

def total_mul(file):
  total = 0
  matches = re.findall(r"mul\(\d+,\d+\)", "".join(file_to_array(file)))
  parsed = [[int(x) for x in row[4:-1].split(",")] for row in matches]
  for pair in parsed:
    total += pair[0] * pair[1]
  return total

def conditional_mul(file):
  total = 0
  matches = re.findall(r"don't|do|mul\(\d+,\d+\)", "".join(file_to_array(file)))
  run_total = True
  for row in matches:
    if row == "do":
      run_total = True
    elif row == "don't":
      run_total = False
    else:
      if not run_total:
        continue
      parsed = [int(x) for x in row[4:-1].split(",")]
      total += parsed[0] * parsed[1]
  return total

assert_equals(total_mul(TEST_INPUT), 161)
print("Part One: ", total_mul(INPUT))
assert_equals(conditional_mul(TEST_INPUT_2), 48)
print("Part Two: ", conditional_mul(INPUT))