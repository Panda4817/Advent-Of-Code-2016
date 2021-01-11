def part1(data):
  n = [
    [1, 2, 3], 
    [4, 5, 6], 
    [7, 8, 9]
  ]
  def isOutside(current):
    if current[0] < 0 or current[0] > 2:
      return True
    elif current[1] < 0 or current[1] > 2:
      return True
    return False
  
  current = [1, 1]
  d = data.split("\n")
  nums = []
  for line in d:
    for c in line:
      if c == 'U':
        current[0] -= 1
        if isOutside(current):
          current[0] += 1
          continue
      elif c == 'D':
        current[0] += 1
        if isOutside(current):
          current[0] -= 1
          continue
      elif c == 'L':
        current[1] -= 1
        if isOutside(current):
          current[1] += 1
          continue
      elif c == 'R':
        current[1] += 1
        if isOutside(current):
          current[1] -= 1
          continue
    nums.append(n[current[0]][current[1]])
    
  return "".join([str(i) for i in nums])

def part2(data):
  n = [
    [0, 0, 1, 0, 0],
    [0, 2, 3, 4, 0], 
    [5, 6, 7, 8, 9], 
    [0, 'A', 'B', 'C', 0],
    [0, 0, 'D', 0, 0,]
  ]
  def isOutside(current):
    if current[0] < 0 or current[0] > 4:
      return True
    elif current[1] < 0 or current[1] > 4:
      return True
    elif n[current[0]][current[1]] == 0:
      return True
    return False
  
  current = [2, 0]
  d = data.split("\n")
  nums = []
  for line in d:
    for c in line:
      if c == 'U':
        current[0] -= 1
        if isOutside(current):
          current[0] += 1
          continue
      elif c == 'D':
        current[0] += 1
        if isOutside(current):
          current[0] -= 1
          continue
      elif c == 'L':
        current[1] -= 1
        if isOutside(current):
          current[1] += 1
          continue
      elif c == 'R':
        current[1] += 1
        if isOutside(current):
          current[1] -= 1
          continue
    nums.append(n[current[0]][current[1]])
    
  return "".join([str(i) for i in nums])