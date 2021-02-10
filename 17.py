import hashlib
from collections import deque
def part1(data):
  start = (0, 0, data)
  end = [3, 3]
  row = [-1, 1, 0, 0]
  col = [0, 0, -1, 1]
  dirs = ["U", "D", "L", "R"]
  letters = ["b", "c", "d", "e", "f"]
  q = deque([start])
  path = ""
  while q:
      r, c, string = q.popleft()
      if r == end[0] and c == end[1]:
          path = string[8:]
          break

      result = hashlib.md5(string.encode())
      hex_hash = result.hexdigest()
      for i in range(4):
          if hex_hash[i] in letters and r + row[i] >= 0 and r + row[i] < 4 and c + col[i] >= 0 and c + col[i] < 4:
              q.append((r + row[i], c + col[i], string + dirs[i]))
  
  return path

def part2(data):
  start = (0, 0, data)
  end = [3, 3]
  row = [-1, 1, 0, 0]
  col = [0, 0, -1, 1]
  dirs = ["U", "D", "L", "R"]
  letters = ["b", "c", "d", "e", "f"]
  q = deque([start])
  steps = 0
  ended = False
  while q:
      if ended == False:
          r, c, string = q.pop()
      else:
          r, c, string = q.popleft()
          ended = False
      if r == end[0] and c == end[1]:
          length = len(string[8:])
          if length > steps:
            steps = length
          ended = True
          continue

      result = hashlib.md5(string.encode())
      hex_hash = result.hexdigest()
      for i in range(4):
          if hex_hash[i] in letters and r + row[i] >= 0 and r + row[i] < 4 and c + col[i] >= 0 and c + col[i] < 4:
              q.append((r + row[i], c + col[i], string + dirs[i]))
  
  return steps