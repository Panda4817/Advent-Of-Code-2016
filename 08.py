import numpy as np

def part1(data):
  grid =  np.zeros((6, 50), dtype='int')
  print(grid)
  instructions = data.split("\n")
  for i in instructions:
    parts = i.split()
    if parts[0] == 'rect':
      nums = [int(n) for n in parts[1].split("x")]
      grid[0: nums[1], 0: nums[0]] = 1
    elif parts[0] == 'rotate' and parts[1] == 'row':
      r = int(parts[2].split("=")[-1])
      num = int(parts[-1])
      row = grid[r: r + 1, 0: 50]
      shifted = np.roll(row, num)
      grid[r: r + 1, 0: 50] = shifted
    elif parts[0] == 'rotate' and parts[1] == 'column':
        h = int(parts[2].split("=")[-1])
        num = int(parts[-1])
        column = grid[0: 6, h: h + 1]
        shifted = np.roll(column, num)
        grid[0: 6, h: h + 1] = shifted
  
  # Part2
  for i in grid:
    for j in i:
      if j == 0:
        print(" ", end="")
      else:
        print(j, end="")
    print()
  return np.count_nonzero(grid == 1)