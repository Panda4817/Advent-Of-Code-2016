a = 0
b = 0
c = 0
d = 0
clock_signal = []

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

def out(num):
  n = convert_to_num(num)
  clock_signal.append(n)
  return n


def part1(data):
  global a, clock_signal
  instructions = data.split("\n")
  length = len(instructions)
  register = 0
  while True:
    index = 0
    nxt = 0
    while(len(clock_signal) < length):
      parts = instructions[index].split()
      if parts[0] == 'out':
        n = out(parts[1])
        if n != nxt:
          break
        elif nxt == 0:
          nxt = 1
        elif nxt == 1:
          nxt = 0
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
    if len(clock_signal) == clock_signal.count(1) + clock_signal.count(0) and len(clock_signal) % 2 == 0:
      j = "".join([str(i) for i in clock_signal])
      if '11' not in j and '00' not in j:
        break
   
    clock_signal.clear()
    register += 1
    a = register
  return register