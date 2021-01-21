def part1(data):
  ips = data.split("\n")
  count = 0
  for ip in ips:
    length = len(ip)
    skip = 0
    inhypernet = False
    match = 0
    for i in range(length-3):
      if skip != 0 and skip != i:
        continue
      skip = 0
      if ip[i] == "[":
        n = i + 1
        while(ip[n] != "]"):
          if ip[n] != ip[n + 1]:
            reverse = ip[n + 1] + ip[n]
            if ip[n+2] + ip[n+3] == reverse:
              inhypernet = True
              break
          n += 1
        if inhypernet:
          break
        skip = n + 1
        continue
      elif ip[i] != ip[i + 1]:
        reverse = ip[i + 1] + ip[i]
        if ip[i+2] + ip[i+3] == reverse:
          match += 1
          skip = i + 4
    
    
    if inhypernet == False and match > 0:
      count += 1
  return count

def part2(data):
  ips = data.split("\n")
  count = 0
  for ip in ips:
    length = len(ip)
    skip = 0
    match = 0
    for i in range(length-2):
      if skip != 0 and skip != i:
        continue
      skip = 0
      if ip[i] == "[":
        x = i + 1
        while (ip[x] != "]"):
          x += 1
        skip = x + 1
        continue
      elif ip[i] != ip[i + 1] and ip[i] == ip[i + 2] and ip[i + 1] != "[":
        reverse = ip[i + 1] + ip[i] + ip[i + 1]
        s = 0
        found = False
        for j in range(length - 2):
          if ip[j] != "[" and s == 0:
            continue
          elif ip[j] == "]":
            s = 0
            continue
          elif ip[j] == "[":
            s = j + 1
          if s != 0 and j != s:
            continue
          if ip[j: j + 3] == reverse:
            match += 1
            found = True
            break
          else:
            s = j + 1
        if found:
          break
    
  
    if match > 0:
      count += 1
  return count
      

