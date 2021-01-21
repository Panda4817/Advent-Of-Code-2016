def part1(data):
  lst = data.split("\n")
  tot = 0
  
  # part 2 - answer variable
  north_pole = 0

  # Part 2 - shift cipher
  def rotate(l, num):
    x = ord(l)
    for i in range(num):
      if x == 122:
        x = 97
      else:
        x += 1
    
    return chr(x)

  for l in lst:
    parts = l.split("-")
    letters = list("".join(parts[0:-1]))
    let_counts = {}
    checksum = parts[-1][4:-1]
    for c in letters:
      if c not in let_counts:
        freq = letters.count(c)
        let_counts[c] = freq
    ordered_counts = sorted(let_counts.items(), key=lambda item: item[0])
    ordered_counts_again = sorted(ordered_counts, key=lambda item: item[1], reverse=True)
    common_five = ordered_counts_again[0:5]
    decoy = False

    for c, o in zip(checksum, common_five):
      if c != o[0]:
        decoy = True
        break
    
    
    if decoy == False:
      num = int(parts[-1][0:3])
      tot += num
      
      # Part 2
      d = ''
      m = " ".join(parts[0:-1])
      for c in m:
        if c == " ":
          d += " "
        else:
          x = rotate(c, num)
          d += x
      if 'north' in d:
        print(d)
        north_pole = num

  
  return tot, north_pole

