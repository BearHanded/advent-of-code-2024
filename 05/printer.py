from functools import cmp_to_key, reduce
from util import assert_equals, file_to_array

INPUT = '05/input.txt'
TEST_INPUT = '05/test_input.txt'

def build_rules(file):
  unparsed = file_to_array(file)
  empty = unparsed.index('')
  rules = [[int(i) for i in row.split("|")] for row in unparsed[:empty]]
  updates = [[int(i) for i in row.split(",")] for row in unparsed[empty + 1:]]
  rules_dict= {}
  for (predecessor, key) in rules:
    if key not in rules_dict:
      rules_dict[key] = {predecessor}
    else:
      rules_dict[key].add(predecessor)

  return rules_dict, updates

def compare_pages(a, b, rules):
  if b in rules and a in rules[b]:
        return -1
  elif a in rules and b in rules[a]:
      return 1
  return 0

def sum_updates(file):
  rules, updates = build_rules(file)
  valid_updates = []

  for update in updates:
    valid = True
    for (idx, page) in enumerate(update):
      preceding = update[:idx]
      if page in rules:
        for target in rules[page]:
          if target in update and target not in preceding:
            valid = False
      if not valid:
        break
    if valid:
      valid_updates.append(update)
  
  return sum([update[(len(update) - 1)//2] for update in valid_updates]) 


def sum_invalid_updates(file):
  rules, updates = build_rules(file)
  invalid = []
  comp = cmp_to_key(lambda a, b: compare_pages(a, b, rules))

  for update in updates:
    valid = True
    for (idx, page) in enumerate(update):
      preceding = update[:idx]
      if page in rules:
        for target in rules[page]:
          if target in update and target not in preceding:
            valid = False
      if not valid:
        sorted_update = sorted(update, key=comp)
        invalid.append(sorted_update)
        break
  
  return sum([update[(len(update) - 1)//2] for update in invalid]) 
assert_equals(sum_updates(TEST_INPUT), 143)
print("Part One: ", sum_updates(INPUT))
assert_equals(sum_invalid_updates(TEST_INPUT), 123)
print("Part Two: ", sum_invalid_updates(INPUT))