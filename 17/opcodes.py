import copy

from util import assert_equals, file_to_subarray

INPUT = 'input.txt'
TEST_INPUT = 'test_input.txt'
TEST_INPUT_2 = 'test_input_2.txt'

#########
# Run
#########
def find_replicating_program(file):
  registers, program = parse(file)
  matches = [0]
  for idx in range(len(program)):
    next_matches = []
    for num in matches:
      for i in range(8):
        candidate = 8 * num + i # Look up entry in next 8 block chunk
        new_registers = copy.deepcopy(registers)
        result = run(new_registers, program, override_a=candidate)
        if result == program:
          return candidate
        if result == program[-(idx+1):]:
          next_matches.append(candidate)
    matches = next_matches


def run_program(file):
  registers, program = parse(file)
  result = run(registers, program)
  return result

def parse(file):
  registers = {}
  register_raw, program_raw = file_to_subarray(file)
  for line in register_raw:
    _, address, value = line.split(" ")
    registers.update({address[:-1]: int(value)})

  program = [int(i) for i in program_raw[0][9:].split(",")]
  return registers, program

def run(registers, program, override_a=0):
  out_arr = []
  pointer = 0
  if override_a:
    registers["A"] = override_a
  while 0 <= pointer < len(program):
    opcode = program[pointer]
    operand = program[pointer + 1]
    pointer = OPERATIONS[opcode](pointer, operand, registers, out_arr)

  return out_arr

#########
# Operations - Why did I do it this way? It was fun
#########
def adv(pointer, operand, registers, out_arr):
  registers["A"] = int(registers["A"] / (2 ** combo(operand, registers)))
  return pointer + 2

def bxl(pointer, operand, registers, out_arr):
  registers["B"] = registers["B"] ^ operand
  return pointer + 2

def bst(pointer, operand, registers, out_arr):
  registers["B"] = combo(operand, registers) % 8
  return pointer + 2

def jnz(pointer, operand, registers, out_arr):
  if registers["A"] == 0:
    return pointer + 2
  return operand

def bxc(pointer, operand, registers, out_arr):
  registers["B"] = registers["B"] ^ registers["C"]
  return pointer + 2

def out(pointer, operand, registers, out_arr):
  value = combo(operand, registers) % 8
  out_arr.append(value)
  return pointer + 2

def bdv(pointer, operand, registers, out_arr):
  registers["B"] = int(registers["A"] / (2 ** combo(operand, registers)))
  return pointer + 2

def cdv(pointer, operand, registers, out_arr):
  registers["C"] = int(registers["A"] / (2 ** combo(operand, registers)))
  return pointer + 2

def combo(value, registers):
  if 0 <= value <= 3:
    return value
  if value == 4:
    return registers["A"]
  if value == 5:
    return registers["B"]
  if value == 6:
    return registers["C"]
  if value == 7:
    raise ValueError("COMBO 7 NOT ALLOWED")


OPERATIONS = {
  0: adv,
  1: bxl,
  2: bst,
  3: jnz,
  4: bxc,
  5: out,
  6: bdv,
  7: cdv
}

#########
# Invoke & Test Suite
#########
test = {"C": 9}
OPERATIONS[2](0, 6, test, [])
assert_equals(test["B"], 1)

test = {"A": 10}
assert_equals(run(test, [5,0,5,1,5,4]), [0,1,2])

test = {"A": 2024}
assert_equals(run(test, [0,1,5,4,3,0]), [4,2,5,6,7,7,7,7,3,1,0])

test = {"B": 29}
OPERATIONS[1](0, 7, test, [])
assert_equals(test["B"], 26)

test = {"B": 2024, "C": 43690}
OPERATIONS[4](0, 0, test, [])
assert_equals(test["B"], 44354)

assert_equals(run_program(TEST_INPUT), [4,6,3,5,6,3,5,2,1,0])
print("Part One: ", run_program(INPUT))

assert_equals(find_replicating_program(TEST_INPUT_2), 117440)
print("Part Two: ", find_replicating_program(INPUT))