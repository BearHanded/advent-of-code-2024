from queue import PriorityQueue
from util import assert_equals, file_to_array

INPUT = 'input.txt'
TEST_INPUT = 'test_input.txt'
DIRS = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def maze_score(file, size, simulation_duration):
  all_falling = [tuple([int(i) for i in row.split(",")]) for row in file_to_array(file, silent=True)]
  falling = set(all_falling[:simulation_duration])
  start = (0, 0)
  end = (size-1, size-1)
  queue = PriorityQueue()
  queue.put((0, start))

  visited = set()
  while not queue.empty():
    score, node = queue.get()
    if node in visited:
      continue
    visited.add(node)
    cost = score + 1
    for next_y, next_x in get_next(node, falling, size, visited):
      if (next_y, next_x) == end:
        return cost
      queue.put((cost, (next_y, next_x)))
  return -1


def get_next(node, obstacles, size, visited):
  available = []
  for direction in DIRS:
    y = node[0] + direction[0]
    x = node[1] + direction[1]
    if not (0 <= y < size) or \
       not (0 <= x < size):
      continue
    if (y, x) in obstacles or (y, x) in visited:
      continue
    available.append((y, x))
  return available

def find_no_escape(file, size, start_i):
  i = start_i
  all_falling = [tuple([int(i) for i in row.split(",")]) for row in file_to_array(file)]

  while True:
    i += 1
    success = maze_score(file, size, i)
    if success == -1:
      return all_falling[i-1]

assert_equals(maze_score(TEST_INPUT, 7, 12), 22)
print("Part One: ", maze_score(INPUT, 71, 1024))
assert_equals(find_no_escape(TEST_INPUT, 7, 12), (6, 1))
print("Part Two: ", find_no_escape(INPUT, 71, 1024))
