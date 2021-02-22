from collections import deque
from itertools import permutations, combinations
from sys import maxsize

def part1(data):
  maze = []
  nums = {}
  start = None
  r_index = 0
  for r in data.split("\n"):
    row = []
    c_index = 0
    for c in r:
      if c == "#":
        row.append(-2)
      elif c == ".":
        row.append(-1)
      else:
        n = int(c)
        row.append(n)
        if n == 0:
          start = (r_index, c_index)
        else:
          nums[n] = (r_index, c_index)
      c_index += 1
    maze.append(row)
    r_index += 1

  perm = [p for p in permutations(nums.keys())]

  nums[0] = start
  combi = [c for c in combinations(nums.keys(), 2)]



  def is_valid(row, col):
    if row < 0 or row >= len(maze):
      return False
    if col < 0 or col >= len(maze[row]):
      return False
    if maze[row][col] < -1:
      return False
    return True

  row = [-1, 0, 0, 1]
  col = [0, 1, -1, 0]

  steps = {}

  # BFS to find shortest path between each position
  for c in combi:
    start = nums[c[0]]
    end = nums[c[1]]
    q = deque([(start, 0)])
    visited = [start]
    while q:
      (r_i, c_i), moves = q.popleft()

      if (r_i, c_i) == end:
        steps[c] = moves
        break

      for i in range(4):
        if is_valid(r_i + row[i], c_i + col[i]) and (r_i + row[i], c_i + col[i]) not in visited:
          q.append(((r_i + row[i], c_i + col[i]), moves + 1))
          visited.append((r_i + row[i], c_i + col[i]))

  lowest_steps = maxsize

  for p in perm:
    lst = list(p)
    lst.insert(0, 0)
    total_steps = 0
    for i in range(len(lst) - 1):
      try:
        total_steps += steps[(lst[i], lst[i+1])]
      except KeyError:
        total_steps += steps[(lst[i + 1], lst[i])]
    
    # Part 2 - Go back to position 0
    try:
      total_steps += steps[(lst[-1], 0)]
    except KeyError:
      total_steps += steps[(0, lst[-1])]
    
    if total_steps < lowest_steps:
      lowest_steps = total_steps
  
  return lowest_steps