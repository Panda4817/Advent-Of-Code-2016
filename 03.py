import itertools

def part1(data):
  lst = data.split("\n")
  valid = len(lst)
  for l in lst:
    nums = [int(i) for i in l.split()]
    combi = list(itertools.combinations(nums, 2))
    for c in combi:
      s = sum(c)
      b = False
      for n in nums:
        if n in c:
          continue
        if s <= n:
          b = True
          valid -= 1
      if b:
        break
  return valid

def part2(data):
  lst = data.split()
  sets = []
  t = []
  for l in range(0, len(lst), 3):
    if len(t) < 3:
      t.append(int(lst[l]))
    if len(t) == 3:
      sets.append(t)
      t = []

  for l in range(1, len(lst), 3):
    if len(t) < 3:
      t.append(int(lst[l]))
    if len(t) == 3:
      sets.append(t)
      t = []
 
  for l in range(2, len(lst), 3):
    if len(t) < 3:
      t.append(int(lst[l]))
    if len(t) == 3:
      sets.append(t)
      t = []
  
  valid = len(sets)
 
  for l in sets:
    combi = list(itertools.combinations(l, 2))
    for c in combi:
      s = sum(c)
      b = False
      for n in l:
        if n in c:
          continue
        if s <= n:
          b = True
          valid -= 1
      if b:
        break
  return valid

  
  
