def part1(data):
  discs = {
    1: [13, 1],
    2: [19, 10],
    3: [3, 2],
    4: [7, 1],
    5: [5, 3],
    6: [17, 5],
    # Part 2 - add another disc
    # 7: [11, 0]
}

  t = 0
  print("running...")
  while True:
      found = True
      for k, v in discs.items():
          a = (k + t + v[1]) % v[0]
          if  a != 0:
              found = False
              break
              
      if found:
          break

      t += 1

  return t