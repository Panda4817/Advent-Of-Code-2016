import hashlib
import re

def part1(data):
  x = 1
  count = 0
  found = False
  password = ''
  while(found == False):
    str_2_hash = data + str(x)
    result = hashlib.md5(str_2_hash.encode())
    hex_hash = result.hexdigest()
    if re.search("^[0]{5}", hex_hash):
      password += hex_hash[5]
      count += 1
    if count == 8:
      found = True
      break
    x += 1
  
  return password

def part2(data):
  x = 1
  count = 0
  found = False
  password = {}
  while(found == False):
    str_2_hash = data + str(x)
    result = hashlib.md5(str_2_hash.encode())
    hex_hash = result.hexdigest()
    if re.search("^[0]{5}", hex_hash):
      try:
        i = int(hex_hash[5])
        if i >= 0 and i <= 7 and i not in password:
          password[i] = hex_hash[6]
          count += 1
      except ValueError as e:
        print(e)  
    if count == 8:
      found = True
      break
    x += 1
  
  return "".join([i[1] for i in sorted(password.items(), key=lambda item: item[0])])