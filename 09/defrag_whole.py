from util import assert_equals, file_as_string

INPUT = 'input.txt'
TEST_INPUT = 'test_input.txt'
OPERATIONS = [lambda x, y: x * y, lambda x, y: x + y, ]
concat_fn = lambda x, y : int(str(x) + str(y))

def checksum(file):
  filesystem = file_as_string(file)
  disk = to_disk(filesystem)
  defragged = defrag(disk)
  print(defragged)

  total = sum(idx * value for idx, value in enumerate(defragged))

  return total


def to_disk(filesystem):
  has_file = True
  disk = []
  for idx, size in enumerate(filesystem):
    label = idx // 2 if has_file else "."
    has_file = not has_file
    disk.append(label * size)
    for _ in range(int(size)):
      disk.append(label)
  return disk

def defrag(disk):
  left = 0
  right = len(disk) - 1


  while left < right:
    left_ready = False
    right_ready = False

    if disk[left] == ".":
      left_ready = True
    else:
      left += 1

    if disk[right] == ".":
      right -= 1
    else:
      right_ready = True

    if left_ready and right_ready:
      disk[left] = disk[right]
      disk[right] = "."
      left += 1
      right -= 1

  return disk

assert_equals(checksum(TEST_INPUT), 2858)
print("Part Two: ", checksum(INPUT))