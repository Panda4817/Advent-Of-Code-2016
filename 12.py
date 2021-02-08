a = 0
b = 0
# part1 is c = 0 and part2 is c = 1
c = 1
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
  else:
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

# same algorithm for part 1 and part 2
def part1(data):
  instructions = data.split("\n")
  print(instructions)
  index = 0
  while(index < len(instructions)):
    parts = instructions[index].split()
    if parts[0] == 'cpy':
      copy(parts[2], parts[1])
    elif parts[0] == 'inc':
      increase(parts[1])
    elif parts[0] == 'dec':
      decrease(parts[1])
    elif parts[0] == 'jnz' and notZero(parts[1]):
      index += int(parts[2])
      continue

    index += 1
  
  return a
    
  

  