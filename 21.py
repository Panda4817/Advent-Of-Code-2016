import copy

def swap_position(p1, p2, s):
    i = int(p1)
    j = int(p2)
    a = s[i]
    b = s[j]
    s[i] = b
    s[j] = a
    return s

def swap_letter(l1, l2, s):
    i = s.index(l1)
    j = s.index(l2)
    s[j] = l1
    s[i] = l2
    return s

def reverse_position(p1, p2, s):
    i = int(p1)
    j = int(p2)
    r = copy.deepcopy(s[i:j + 1])
    r.reverse()
    return s[0:i] + r + s[j + 1:]

def move_positions(i1, i2, s):
    l = s.pop(int(i1))
    s.insert(int(i2), l)
    return s

def rotate_right(num, s):
    n = int(num)
    if n % len(s) == 0:
        return s
    for i in range(n):
        l = s.pop()
        s.insert(0, l)
    return s

def rotate_left(num, s):
    n = int(num)
    if n % len(s) == 0:
        return s
    for i in range(n):
        l = s.pop(0)
        s.append(l)
    return s

def rotate_position(l, s):
    index = s.index(l)
    rot = index + 1
    if index >= 4:
        rot += 1
    return rotate_right(rot, s)

def rotate_position_opp(l, s):
    index = s.index(l)
    for i in range(len(s)):
        rot = i + 1
        if i >= 4:
            rot += 1
        new_i = i
        for j in range(rot):
            new_i += 1
            if new_i == len(s):
                new_i = 0
        if new_i == index:
            break
    return rotate_left(rot, s)
  
def part1(data):
  instructions = [l.split() for l in data.split("\n")]
  s = list("abcdefgh")
  for i in instructions:
    cp = copy.deepcopy(s)
    if i[0] == "swap":
        if i[1] == "position":
            s = swap_position(i[2], i[5], cp)
        elif i[1] == "letter":
            s = swap_letter(i[2], i[5], cp)
    elif i[0] == "rotate":
        if i[1] == "left":
            s = rotate_left(i[2], cp)
        elif i[1] == "right":
            s = rotate_right(i[2], cp)
        elif i[1] == "based":
            s = rotate_position(i[6], cp)
    elif i[0] == "reverse":
        s = reverse_position(i[2], i[4], cp)
    elif i[0] == "move":
        s = move_positions(i[2], i[5], cp)
  
  return "".join(s)

def part2(data):
  instructions = [l.split() for l in data.split("\n")]
  instructions.reverse()
  s = list("fbgdceah")
  for i in instructions:
    cp = copy.deepcopy(s)
    print(i, cp)
    if i[0] == "swap":
        if i[1] == "position":
            s = swap_position(i[2], i[5], cp)
        elif i[1] == "letter":
            s = swap_letter(i[2], i[5], cp)
    elif i[0] == "rotate":
        if i[1] == "left":
            s = rotate_right(i[2], cp)
        elif i[1] == "right":
            s = rotate_left(i[2], cp)
        elif i[1] == "based":
            s = rotate_position_opp(i[6], cp)
    elif i[0] == "reverse":
        s = reverse_position(i[2], i[4], cp)
    elif i[0] == "move":
        s = move_positions(i[5], i[2], cp)
  
  return "".join(s)