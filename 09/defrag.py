from util import assert_equals, file_as_string

INPUT = 'input.txt'
TEST_INPUT = 'test_input.txt'
OPERATIONS = [lambda x, y: x * y, lambda x, y: x + y, ]
concat_fn = lambda x, y : int(str(x) + str(y))

def checksum(file, whole_file=False):
  filesystem = file_as_string(file)
  disk = to_disk(filesystem)
  defragged = defrag_whole(disk) if whole_file else defrag(disk)

  total = sum((idx * value if value != "." else 0) for idx, value in enumerate(defragged))

  return total


def to_disk(filesystem):
  has_file = True
  disk = []
  for idx, size in enumerate(filesystem):
    label = idx // 2 if has_file else "."
    has_file = not has_file
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

  return [i for i in disk if i != "."]

def defrag_whole(disk):
  right = len(disk) - 1

  while right > 0:
    right_b = right
    left_size = 0
    right_size = 0

    # Find rightmost file
    if disk[right] == ".":
      right -= 1
      continue
    else:
      right_b = right
      while True:
        if disk[right_b - 1] == disk[right]:
          right_b -= 1
        else:
          break
      right_size = right - right_b + 1

    left = 0
    # check gaps
    while left < right_b:
      left_b = left
      if disk[left] == ".":
        while True:
          if disk[left_b + 1] == ".":
            left_b += 1
          else:
            break
        left_size = left_b - left + 1
        if left_size >= right_size:
          # do the thing
          disk[left : left+right_size] = disk[right_b:right+1]
          disk[right_b:right+1] = ["."] * right_size
          break
        else:
          left = left_b + 1
      else:
        left += 1

    right = right_b - 1

  return disk
assert_equals(checksum(TEST_INPUT), 1928)
print("Part One: ", checksum(INPUT))
assert_equals(checksum(TEST_INPUT, whole_file=True), 2858)
print("Part Two: ", checksum(INPUT, whole_file=True))