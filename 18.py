def part1(data):
  first_row = [False if i == "." else True for i in data]
  l = len(first_row)
  num_rows = 40 # part 1
  # num_rows = 400000 # part 2
  count = first_row.count(False)
  grid = [[False for c in range(l)] for r in range(num_rows)]
  grid[0] = first_row
  for r in range(1, num_rows):
      for c in range(l):
          if c == 0:
              traps = [False, grid[r - 1][c], grid[r - 1][c + 1]]
          elif c == l - 1:
              traps = [grid[r - 1][c - 1], grid[r - 1][c], False]
          else:
              traps = [grid[r - 1][c - 1], grid[r - 1][c], grid[r - 1][c + 1]]
          
          if traps == [True, True, False] or traps == [False, True, True] or traps == [True, False, False] or traps == [False, False, True]:
              grid[r][c] = True
          else:
              grid[r][c] = False
              count += 1
  return count