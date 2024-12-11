from collections import Counter
from util import assert_equals, file_as_string

INPUT = 'input.txt'
TEST_INPUT = 'test_input.txt'

def stone_count(file, blinks):
  stones = [int(i) for i in file_as_string(file).split(" ")]

  stone_counter = Counter(stones) # track total rocks of each num
  for _ in range(blinks):
    # start fresh each time, transform the rocks
    new_counter = Counter()
    for stone in stone_counter.keys():
      for new_stone in blink_stone(stone):
        new_counter[new_stone] += stone_counter[stone]
    stone_counter = new_counter
  return sum(stone_counter.values())

def blink_stone(stone):
  str_stone = str(stone)
  if stone == 0:
    return [1]
  elif len(str_stone) % 2 == 0:
    pivot = len(str_stone) // 2
    stone_a, stone_b = int(str_stone[:pivot]), int(str_stone[pivot:])
    return [stone_a, stone_b]
  return [stone * 2024]

assert_equals(stone_count(TEST_INPUT, 25), 55312)
print("Part One: ", stone_count(INPUT, 25))
print("Part Two: ", stone_count(INPUT, 75))