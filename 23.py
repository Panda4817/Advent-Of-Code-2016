
a = 7
b = 0
c = 0
d = 0

def convert_to_num(num):
  global a, b, c, d
  try:
    num = int(num)
  except ValueError:
    if num == 'a':
      num = a
    elif num == 'b':
      num = b
    elif num == 'c':
      num = c
    else:
      num = d
  return num

def copy(v, num):
  global a, b, c, d
  n = convert_to_num(num)
  if v == 'a':
    a = n
  elif v == 'b':
    b = n
  elif v == 'c':
    c = n
  elif v == 'd':
    d = n

def increase(v):
  global a, b, c, d
  if v == 'a':
    a += 1
  elif v == 'b':
    b += 1
  elif v == 'c':
    c += 1
  else:
    d += 1

def decrease(v):
  global a, b, c, d
  if v == 'a':
    a -= 1
  elif v == 'b':
    b -= 1
  elif v == 'c':
    c -= 1
  else:
    d -= 1

def notZero(num):
  n = convert_to_num(num)
  if n != 0:
    return True
  return False

def toggle(num, instructions, index):
  n = convert_to_num(num)
  try:
    parts = instructions[index + n].split()
    if parts[0] == 'inc':
      parts[0] = 'dec'
    elif parts[0] == 'dec' or parts[0] == 'tgl':
      parts[0] = 'inc'
    elif parts[0] == 'jnz':
      parts[0] = 'cpy'
    else:
      parts[0] = 'jnz'
    instructions[index + n] = " ".join(parts)
    return instructions
  except IndexError:
    return instructions


def part1(data):
  instructions = data.split("\n")
  length = len(instructions)
  index = 0
  while(index < length):
    parts = instructions[index].split()
    if parts[0] == 'tgl':
      instructions = toggle(parts[1], instructions, index)
      print(instructions)
    elif parts[0] == 'cpy':
      copy(parts[2], parts[1])
    elif parts[0] == 'inc':
      increase(parts[1])
    elif parts[0] == 'dec':
      decrease(parts[1])
    elif parts[0] == 'jnz' and notZero(parts[1]):
      n = convert_to_num(parts[2])
      index += n
      continue

    index += 1
  
  return a

def part2(data):
  # start with a = 6, end with a = 6341
  # start with a = 7, end with a = 10661
  # start with a = 8, end with a = 45941
  # pattern is (6341 * 7 (next_a_number)) - 33726 ((6341*7) - 10661)
  # then add 5621 to 33728
  # for a = 8, 45941 = 10661 * 8 - (33721 + 5621)

  start_a = 8
  end_a = 10661
  subtraction = 33726
  factor = 5621
  while start_a != 13:
    subtraction = subtraction + factor
    end_a = end_a * start_a - subtraction
    print(start_a, end_a, subtraction)
    start_a += 1
  
  return end_a



