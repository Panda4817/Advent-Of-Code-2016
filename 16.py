def part1(data):
  string = data

  # Part 1
  # space = 272
  # Part 2
  space = 35651584

  def dragon_curve(string, space):
      if len(string) >= space:
          return string
      
      a = string
      b = string[::-1]
      c = ''
      for char in b:
          if char == '1':
              c += '0'
          else:
              c += '1'

      d = a + '0' + c
      return dragon_curve(d, space)

  def get_checksum(string, calculated):
      if calculated > 0 and len(string) % 2 != 0:
          return string
      
      checksum = ''
      for i in range(0, len(string), 2):
          if string[i] == string[i + 1]:
              checksum += '1'
          else:
              checksum += '0'
      
      return get_checksum(checksum, calculated + 1)


  new_string = dragon_curve(string, space)
  checksum = get_checksum(new_string[0:space], 0)
  return checksum
