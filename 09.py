def part1(data):
  decompressed = ""
  tot_length = len(data)
  skip = 0
  for i in range(tot_length):
    if skip != 0 and skip != i:
      continue
    skip = 0
    if data[i] == '(':
      first = ''
      x = i
      while (data[x] != "x"):
        x += 1
        if data[x] == "x":
          break
        first += data[x]
      length = int(first)
      last =""
      while (data[x] != ")"):
        x += 1
        if data[x] == ")":
          break
        last += data[x]
      repeat = int(last)
      skip = x + length + 1
      for r in range(repeat):
        decompressed += data[x + 1:x + length + 1]
    else:
      decompressed += data[i]
  
  return len(decompressed)

def part2(data):

  def recurse(string):
    decompressed = 0
    tot_length = len(string)
    skip = 0
    for i in range(tot_length):
      if skip != 0 and skip != i:
        continue
      skip = 0
      if string[i] == '(':
        first = ""
        x = i
        while (string[x] != "x"):
          x += 1
          if string[x] == "x":
            break
          first += string[x]
        length = int(first)
        last = ""
        while (string[x] != ")"):
          x += 1
          if string[x] == ")":
            break
          last += string[x]
        repeat = int(last)
        skip = x + length + 1
        decompressed += repeat * recurse(string[x + 1:x + length + 1])
      else:
        decompressed += 1
    
    return decompressed
  
  decompressed = recurse(data)
  return decompressed


      