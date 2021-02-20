import numpy as np
from queue import PriorityQueue
from dataclasses import dataclass, field
from typing import Any

class Node():
    def __init__(self, name, size, used, avail, use):
        self.name = name
        self.size = size
        self.used = used
        self.avail = avail
        self.use = use
        lst = self.name.split("y")
        self.row_col = (int(lst[1]), int(lst[0][1:]))
    
    def __str__(self):
        return f'name: {self.name} - size: {self.size} - used: {self.used} - avail: {self.avail} - use {self.use}%'
    
    def __eq__(self, other):
        return self.name == other.name
    
    def move_data_in(self, other):
        if other.used > self.size:
            return False
        return True

@dataclass(order=True)
class PrioritizedItem:
    priority: int
    node: Any=field(compare=False)
    moves: int=field(compare=False)

def part1(data):
  lst = data.split("\n")[2:]

  grid = []
  row = []
  for l in lst:
      parts = l.split()
      name = parts[0].split("-")
      node = Node("".join(name[1:]), int(parts[1][0:-1]), int(parts[2][0:-1]), int(parts[3][0:-1]), int(parts[4][0:-1]))
      row.append(node)
      if int(name[2][1:]) == 29:
          grid.append(row)
          row = []

  grid = np.array(grid)
  grid = np.rot90(grid)
  grid = np.flipud(grid)

  pairs = []
  empty = None
  a = None
  for r in grid:
      for c in r:
          if c.used != 0:
              a = c
          else:
              empty = c
          for r in grid:
              for c in r:
                  if a == c:
                      continue
                  if a.used <= c.avail and (a, c) not in pairs:
                      pairs.append((a, c))
  
  return grid, empty, len(pairs)

def part2(data):
  grid, start, pairs = part1(data)
  num_of_rows = len(grid)
  num_of_cols = len(grid[0])
  end = grid[0:1, num_of_cols - 2:num_of_cols - 1][0][0]

  total_steps = 0

  row = [-1, 0, 0, 1]
  col =[0, 1, -1, 0]

  def is_valid(r,c):
      if r < 0 or r >= num_of_rows:
          return False
      if c < 0 or c >= num_of_cols:
          return False
      return True

  def get_h(endNode, startNode):
      h = abs(endNode.row_col[0] - startNode.row_col[0]) + abs(endNode.row_col[1] - startNode.row_col[1])
      return h

  goal_data = grid[0:1, num_of_cols-1:num_of_cols][0][0]

  while True:
      h = get_h(end, start)
      q = PriorityQueue()
      q.put(PrioritizedItem(total_steps + h, start, total_steps))
      visited = {start.name: (start, total_steps), goal_data.name: (goal_data, 0)}
      
      while q:
          obj = q.get()
          node = obj.node
          moves = obj.moves
          if node.row_col == end.row_col:
              total_steps = moves + 1
              break
          for i in range(4):
              r, c = node.row_col
              if is_valid(r + row[i], c + col[i]):
                  other = grid[r+row[i]:r+row[i]+1, c+col[i]:c+col[i]+1][0][0]
                  if node.move_data_in(other):
                      if other.name not in visited or moves + 1 < visited[other.name][1]:
                          h = get_h(end, other)
                          q.put(PrioritizedItem(moves + 1 + h, other, moves + 1))
                          visited[other.name] = (other, moves + 1)
      if end.row_col == (0, 0):
          break
      goal_data = node
      r, c = node.row_col
      start = grid[r: r+1, c+1:c+2][0][0]
      end = grid[r:r+1, c-1:c][0][0]
  
  return total_steps
