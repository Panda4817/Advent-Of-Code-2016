import copy

def part1(data):
  instructions = data.split("\n")
  bots = {}
  outputs = {}
  other = []

  def place_in_bots(num, value):
    if num not in bots:
        bots[num] = []
    if value not in bots[num]:
      bots[num].append(value)


  for i in instructions:
    parts = i.split()
    if parts[0] == 'value':
      bot_num = int(parts[-1])
      value_num = int(parts[1])
      place_in_bots(bot_num, value_num)
    elif 'output' in parts:
      other.append([int(p) if p.isnumeric() else p for p in parts])
      for p in parts:
        if p == 'output':
          index = parts.index(p) + 1
          output_num = int(parts[index])
          outputs[output_num] = []
    else:
      other.append([int(p) if p.isnumeric() else p for p in parts])

  while(True):
    copy_bots = copy.deepcopy(bots)
    for k, v in copy_bots.items():
      if len(v) != 2:
        continue
      low = min(v)
      high = max(v)
      # Part 1
      # if low == 17 and high == 61:
      #   return k
      for o in other:
        if o[1] != k:
          continue
        if o[5] == 'output':
          outputs[o[6]].append(low)
        else:
          place_in_bots(o[6], low)
        bots[k].remove(low)
        if o[-2] == 'output':
          outputs[o[-1]].append(high)
        else:
          place_in_bots(o[-1], high)
        bots[k].remove(high)
        break
    # Part 2
    if len(outputs[0]) == 1 and len(outputs[1]) == 1 and len(outputs[2]) == 1:
      break
  
  return outputs[0][0] * outputs[1][0] * outputs[2][0]
    
      
  


