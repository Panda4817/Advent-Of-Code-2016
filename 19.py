class Node():
    def __init__(self, data=1, next_node=None, prev_node=None):
        self.skipped = False
        self.data = data
        self.next_node = next_node
        self.prev_node = prev_node
    
    def add_next_node(self, node):
        self.next_node = node
    
    def add_prev_node(self, node):
        self.prev_node = node
    
    
    def find_opposite(self, middle):
        current = self
        num = 0
        while num != middle:
            current = current.next_node
            num += 1
        return current
    
    def __str__(self):
        return f"{self.data} - skipped:{self.skipped} - next:{self.next_node.data} - prev:{self.prev_node.data}"


def part1(data):
  elves = int(data)
  start = Node()
  current = start
  for i in range(2, elves + 1):
    if i == elves:
      next_node = Node(i, start)
      current.add_next_node(next_node)
      current = start
    else:
      next_node = Node(i)
      current.add_next_node(next_node)
      current = next_node

  def skip_next(node):
    if node.skipped == False:
      return node
    return skip_next(node.next_node)

  num_removed = 0
  while num_removed != elves - 1:
    if current.skipped == False:
      next_node = skip_next(current.next_node)
      next_node.skipped = True
      current.add_next_node(next_node.next_node)
      num_removed += 1
    current = current.next_node
  return current.data

def part2(data):
  elves = int(data)
  start = Node()
  current = start
  last = Node(elves, start)
  prev = last
  for i in range(2, elves + 1):
      if i == elves:
          next_node = last
          current.add_next_node(next_node)
          current.add_prev_node(prev)
          prev = current
          current = next_node
          current.add_prev_node(prev)
          current = current.next_node
      else:
          next_node = Node(i)
          current.add_next_node(next_node)
          current.add_prev_node(prev)
          prev = current
          current = next_node
      

  num_removed = 0
  current_opp = None
  prev_middle = None
  while True:
      if current.skipped == False:
          middle = (elves - num_removed) // 2
          if current_opp == None:
              opp_node = current.find_opposite(middle)
          else:
              if middle == prev_middle:
                  opp_node = current_opp.next_node.next_node
              elif middle < prev_middle:
                  opp_node = current_opp.next_node
          opp_node.skipped = True
          opp_node.prev_node.add_next_node(opp_node.next_node)
          opp_node.next_node.add_prev_node(opp_node.prev_node)
          num_removed += 1
          current_opp = opp_node
          prev_middle = middle
          if num_removed == elves - 1:
              break
      current = current.next_node
  return current.data

