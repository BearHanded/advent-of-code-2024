from util import assert_equals, file_to_array

INPUT = 'input.txt'
TEST_INPUT = 'test_input.txt'

def count_antinodes(file):
  antenna_map = file_to_array(file)
  antennas = {}
  antinodes = set()

  for y, row in enumerate(antenna_map):
    for x, cell in enumerate(row):
      if cell != ".":
        if cell not in antennas:
          antennas.update({cell: [(y, x)]})
        else:
          antennas[cell].append((y, x))

  for group in antennas:
    for a in antennas[group]:
      for b in antennas[group]:
        if a == b:
          continue
        antinode_a = (2*a[0]-b[0], 2*a[1]-b[1])
        antinode_b = (2*b[0]-a[0], 2*b[1]-a[1])
        if 0 <= antinode_a[0] < len(antenna_map) and  0 <= antinode_a[1] < len(antenna_map[1]):
          antinodes.add(antinode_a)
        if 0 <= antinode_b[0] < len(antenna_map) and  0 <= antinode_b[1] < len(antenna_map[1]):
          antinodes.add(antinode_b)
  return len(antinodes)


def more_antinodes(file):
  antenna_map = file_to_array(file)
  antennas = {}
  antinodes = set()

  for y, row in enumerate(antenna_map):
    for x, cell in enumerate(row):
      if cell != ".":
        if cell not in antennas:
          antennas.update({cell: [(y, x)]})
        else:
          antennas[cell].append((y, x))

  for group in antennas:
    if len(antennas[group]) == 1:
      continue

    for a in antennas[group]:
      for b in antennas[group]:
        if a == b:
          continue
        y = a[0] - b[0]
        x = a[1] - b[1]

        cursor = a
        while 0 <= cursor[0] < len(antenna_map) and 0 <= cursor[1] < len(antenna_map[1]):
          antinodes.add(cursor)
          cursor = cursor[0] + y, cursor[1] + x

        cursor = b
        while 0 <= cursor[0] < len(antenna_map) and 0 <= cursor[1] < len(antenna_map[1]):
          antinodes.add(cursor)
          cursor = cursor[0] - y, cursor[1] - x
  return len(antinodes)

assert_equals(count_antinodes(TEST_INPUT), 14)
print("Part One: ", count_antinodes(INPUT))
assert_equals(more_antinodes(TEST_INPUT), 34)
print("Part Two: ", more_antinodes(INPUT))