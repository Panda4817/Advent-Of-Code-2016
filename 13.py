import sys
from collections import deque

def part1(data):
  start = (1, 1, 0)
  endRow = 39
  endCol = 31
  q = deque()
  q.append(start)

  # part 1
  # min_dist = sys.maxsize

  fav = int(data)
  visited = [[False for i in range(endCol + 2)] for j in range(endRow + 2)]

  r = [1, 0, -1, 0]
  c = [0, 1, 0, -1]

  def isValid(r, c):
      if r < 0 or r > endRow + 1 or c < 0 or c > endCol + 1:
          return False
      
      if visited[r][c]:
          return False

      v = c * c + 3 * c + 2 * c * r + r + r * r
      v += fav

      n = bin(v).count('1')
      if n % 2 != 0:
          return False
      
      return True

  # part 2
  reached = []

  while q:
      row, col, dist = q.popleft()
      visited[row][col] = True
      
      # Part 2
      if dist <= 50 and (row, col) not in reached:
          reached.append((row, col))
      
      # Part 1
      # if row == endRow and col == endCol:
      #     min_dist = dist
      #     break

      if dist > 50:
          break

      for i in range(4):
          if isValid(row + r[i], col + c[i]):
              q.append((row + r[i], col + c[i], dist + 1))

  return len(reached)