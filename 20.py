# Part 2 in part 1
def part1(data):
  ranges = sorted([[int(i) for i in d.split("-")] for d in data.split("\n")], key=lambda x: x[1])
  ranges = sorted(ranges, key=lambda x: x[0])
  high = 4294967295

  num = 0
  length = len(ranges)
  lowest = high
  highest = 0
  for i in range(length - 1):
      current = ranges[i]
      next = ranges[i + 1]
      diff = next[0] - current[1]
      if diff > 1:
          if current[1] + 1 < lowest:
              lowest = current[1] + 1
          # part 1
          for j in range(current[1] + 1, next[0]):
              if j > highest:
                num += 1
      if next[1] > highest:
          highest = next[1]
          

  return (lowest, num)
