# Part 1 and 2 in part1 fu
def part1(data):
  d = data.split(", ")
  current = (0, 0)
  facing = 'N'
  grid = [(0, 0)]
  twice = None
  for i in d:
    n = int(i[1:])
    t = i[0]
    if facing == 'N':
      if t == 'R':
        # Part 2
        for j in range(1, n):
          c = (current[0] + j, current[1])
          if c in grid:
            twice = c
            break
          grid.append(c)
        # Part 1
        new = (current[0] + n, current[1])
        facing = 'W'
      
      elif t == 'L':
        # Part 2
        for j in range(1, n):
          c = (current[0] - j, current[1])
          if c in grid:
            twice = c
            break
          grid.append(c)
         # Part 1
        new = (current[0] - n, current[1])
        facing = 'E'
    
    elif facing == 'S':
      if t == 'R':
        # Part 2
        for j in range(1, n):
          c = (current[0] - j, current[1])
          if c in grid:
            twice = c
            break
          grid.append(c)
         # Part 1
        new = (current[0] - n, current[1])
        facing = 'E'
      
      elif t == 'L':
        # Part 2
        for j in range(1, n):
          c = (current[0] + j, current[1])
          if c in grid:
            twice = c
            break
          grid.append(c)
         # Part 1
        new = (current[0] + n, current[1])
        facing = 'W'
    
    elif facing == 'E':
      if t == 'R':
        # Part 2
        for j in range(1, n):
          c = (current[0], current[1] + j)
          if c in grid:
            twice = c
            break
          grid.append(c)
         # Part 1
        new = (current[0], current[1] + n)
        facing = 'N'
      
      elif t == 'L':
        # Part 2
        for j in range(1, n):
          c = (current[0], current[1] - j)
          if c in grid:
            twice = c
            break
          grid.append(c)
         # Part 1
        new = (current[0], current[1] - n)
        facing = 'S'
    
    elif facing == 'W':
      if t == 'R':
        # Part 2
        for j in range(1, n):
          c = (current[0], current[1] - j)
          if c in grid:
            twice = c
            break
          grid.append(c)
         # Part 1
        new = (current[0], current[1] - n)
        facing = 'S'
      
      elif t == 'L':
        # Part 2
        for j in range(1, n):
          c = (current[0], current[1] + j)
          if c in grid:
            twice = c
            break
          grid.append(c)
         # Part 1
        new = (current[0], current[1] + n)
        facing = 'N'
    current = new
    
    # Part 2
    if new not in grid:
      grid.append(new)
    else:
      break
    
    if twice != None:
      break

  return abs(twice[0]) + abs(twice[1]) #abs(current[0]) + abs(current[1])