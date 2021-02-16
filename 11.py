from copy import deepcopy
from itertools import combinations
from queue import PriorityQueue


class GameState(object):

    def __init__(self, floors, lift_floor=1, moves=0):
        self.floors = floors
        self.lift_floor = lift_floor
        self.moves = moves
        self.num_floors = len(floors)


    @property
    def uid(self):
        uid = str(self.lift_floor)
        for fl in range(1, self.num_floors + 1):
            uid += str(fl) + ''.join(sorted([it[-1] for it in self.floors[fl]]))
        return uid

    @property
    def won(self):
        won = True
        for fl in range(1, self.num_floors):
            if self.floors[fl]:
                won = False
                break
        return won

    @staticmethod
    def validate_floors(floors):
        for items in floors.values():
            microchips = set(i[:-1] for i in items if i.endswith('m'))
            generators = set(i[:-1] for i in items if i.endswith('g'))
            unpaired_microchips = microchips - generators
            if unpaired_microchips and generators:
                return False
        return True

    def possible_floors(self):
        """
        Adjacent floors that could be moved to
        """
        if self.lift_floor == 1:
            return (2,)
        elif self.lift_floor == self.num_floors:
            return (self.lift_floor - 1,)
        else:
            return self.lift_floor + 1, self.lift_floor - 1

    def possible_items(self):
        """
        All combinations of single and pairs of items on the current floor
        """
        available_items = self.floors[self.lift_floor]
        single_items = [(i,) for i in available_items]
        double_items = [i for i in combinations(available_items, 2)]
        return single_items + double_items

    @property
    def possible_moves(self):
        """
        The possible next states after making a move
        """
        states = []
        possible_floors = self.possible_floors()
        possible_items = self.possible_items()

        for fl in possible_floors:
            for items in possible_items:
                new_floors = deepcopy(self.floors)
                for item in items:
                    new_floors[self.lift_floor].remove(item)
                    new_floors[fl].append(item)

                if self.validate_floors(new_floors):
                    states.append(
                        GameState(new_floors, lift_floor=fl, moves=self.moves+1)
                    )

        return states

    @property
    def f(self):
        """
        A* cost for this game state
        """
        return self.g() + self.h()

    def g(self):
        """
        Number of moves between initial state and current state
        """
        return self.moves

    def h(self):
        """
        Heuristic of estimated moves from current state to end state
        """
        cost = 0
        for fl in range(1, self.num_floors):
            cost += len(self.floors[fl]) * (self.num_floors - fl)
        return cost

def part1(data):
  test_config = {
      1: ['hm', 'lm'],
      2: ['hg'],
      3: ['lg'],
      4: [],
  }

  # part1 config
  config = {
      1: ['dg', 'dm'],
      2: ['ag', 'bg', 'cg', 'eg'],
      3: ['am', 'bm', 'cm', 'em'],
      4: [],
  }
  # Part2 config
  # config = {
  #     1: ['dg', 'dm', 'fg', 'fm', 'gg', 'gm'],
  #     2: ['ag', 'bg', 'cg', 'eg'],
  #     3: ['am', 'bm', 'cm', 'em'],
  #     4: [],
  # }

  start = GameState(config)

  q = PriorityQueue()
  q.put((start.f, start.uid,))
  visited = {start.uid: start}

  while not q.empty():
      pri, node_uid = q.get()
      node = visited[node_uid]

      #print(pri, node_uid, node.moves, node.floors)

      if node.won:
          print(f'Won in {node.moves} moves')
          return node.moves

      for n in node.possible_moves:
          # Append new or better states to the queue and mark them as visited
          if n.uid not in visited or n.moves < visited[n.uid].moves:
              visited[n.uid] = n
              q.put((n.f, n.uid,))
          #print(len(visited), q.qsize())
  