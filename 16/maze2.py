from queue import PriorityQueue

from util import assert_equals, file_to_array

INPUT = 'input.txt'
TEST_INPUT = 'test_input.txt'
TEST_INPUT_2 = 'test_input_2.txt'
DIRS = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def maze_score(file):
  maze = file_to_array(file)
  start = None
  end = None
  queue = PriorityQueue()
  # parse
  for y, row in enumerate(maze):
    for x, cell in enumerate(row):
      if cell == "S":
        start = (y, x)
      elif cell == "E":
        end = (y, x)

  queue.put((0, start, (0, 1), {start}))

  # explore
  visited = set()
  best_seats = set()
  low_score = 100000000000
  while not queue.empty():
    score, node, direction, path_seats = queue.get()
    visited.add((node, direction))
    for next_dir, cost in score_directions(direction, score):
      next_y = node[0] + next_dir[0]
      next_x = node[1] + next_dir[1]
      new_seats = path_seats.union({(next_y, next_x)})

      if maze[next_y][next_x] == "#" or \
         ((next_y, next_x), next_dir) in visited or \
        cost > low_score:
        continue
      if (next_y, next_x) == end:
        low_score = cost
        best_seats.update(new_seats)
        continue
      queue.put((cost, (next_y, next_x), next_dir, new_seats))

  return len(best_seats)


def score_directions(direction, score):
  l = ((direction[1] * -1, direction[0]), score + 1001)
  r = ((direction[1], direction[0] * -1), score + 1001)
  s = (direction, score + 1)
  return [l, r, s]

assert_equals(maze_score(TEST_INPUT), 45)
assert_equals(maze_score(TEST_INPUT_2), 64)
print("Part One: ", maze_score(INPUT))
