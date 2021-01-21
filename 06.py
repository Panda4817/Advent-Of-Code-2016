def part1(data):
  mgs = data.split("\n")

  positions = {i : '' for i in range(8)}
  
  for m in mgs:
    for i in range(8):
      positions[i] += m[i]

  for p, s in positions.items():
    highest_freq = 0
    current_highest = ''
    for c in s:
      num = 0
      for ch in s:
        if c == ch:
          num += 1
      if num > highest_freq:
        highest_freq = num
        current_highest = c
    positions[p] = current_highest
  
  return "".join(positions.values())

def part2(data):
  mgs = data.split("\n")

  positions = {i : '' for i in range(8)}
  
  for m in mgs:
    for i in range(8):
      positions[i] += m[i]
      
  for p, s in positions.items():
    lowest_freq = float('inf')
    current_lowest = ''
    for c in s:
      num = 0
      for ch in s:
        if c == ch:
          num += 1
      if num < lowest_freq:
        lowest_freq = num
        current_lowest = c
    positions[p] = current_lowest
  
  return "".join(positions.values())