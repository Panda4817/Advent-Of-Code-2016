import hashlib
import re

def part1(data):
  data = data
  total_keys = 64
  three = re.compile(r'(.)\1\1')
  num = 0
  key_count = set()
  indices= {}
  
  # Part 2
  stretch_factor = 2016
  
  while len(key_count) < total_keys:
      str_2_hash = data + str(num)
      result = hashlib.md5(str_2_hash.encode())
      hex_hash = result.hexdigest()

      # Part 2
      for i in range(stretch_factor):
          result = hashlib.md5(hex_hash.encode())
          hex_hash = result.hexdigest()
      
      result1 = three.findall(hex_hash)
      if len(result1) > 0:
          indices[(num, num + 1, num + 1000)] = result1[0]

      for k, v in indices.items():
          if num < k[1] or num > k[2]:
              continue
          
          five = re.compile(rf'({v})\1\1\1\1')
          result2 = five.search(hex_hash)
          if  result2 != None:
              key_count.add(k[0])
          
          if len(key_count) == total_keys:
              break
          
      num += 1

  return max(key_count)