import itertools

class Graph:
  class EdgesType:
    FORWARD = "F"
    CROSS = "C"
    BACK = "B"
    UNMARKED = "U"

  def __init__(self, graph_ascii = ''):
    self.adj_list = {}

    edges = graph_ascii.split("\n")
    source_vertex = 0
    for edge in edges:
      destination_vertex = 0
      self.adj_list[source_vertex] = []
      for bit in edge:
        if bit == '1':
          self.adj_list[source_vertex].append((destination_vertex, Graph.EdgesType.UNMARKED))
        destination_vertex += 1
      source_vertex += 1

  def print(self):
    for v1 in self.adj_list:
      print(chr(v1 + ord('A')), end="->")
      for (v2, et) in self.adj_list[v1]:
        print(chr(v2 + ord('A')) + '(' + et + ')', end=" ")
      print()

  # O(E)
  def bfs(self, start = 0):
    level = {start: 0}
    frontiers = {start}
    parent = {start: -1}
    cur_level = 1

    while frontiers:
      next_frontiers = set()
      for frontier in frontiers:
        for (adj_vertex, _) in self.adj_list[frontier]:
          if not adj_vertex in level:
            level[adj_vertex] = cur_level
            parent[adj_vertex] = frontier
            next_frontiers.add(adj_vertex)

      frontiers = next_frontiers
      cur_level += 1

    return (parent, level)

  def shortest_path(self, start, destination):
    (parent, level) = self.bfs(start)
    if destination in level:
      return level[destination]
    else:
      return None

  # O(E)
  def dfs(self, start = 0):
    level = {start: 0}
    parent = {start: -1}

    def visit(start, cur_level):
      for (v, _) in self.adj_list[start]:
        if not v in parent:
          parent[v] = start
          level[v] = cur_level
          visit(v, cur_level + 1)

    visit(start, 1)
    return (parent, level)

  # O(E + V)
  def categorize_edges(self):
    parent = {}
    cur_parent = {}
    cur_stack = set()

    def visit(start):
      for i in range(len(self.adj_list[start])):
        v = self.adj_list[start][i][0]
        if v in parent:
          self.adj_list[start][i] = (v, Graph.EdgesType.CROSS)
        elif not v in cur_stack:
          cur_parent[v] = start
          self.adj_list[start][i] = (v, Graph.EdgesType.FORWARD)
          cur_stack.add(start)
          visit(v)
          cur_stack.remove(start)
        else:
          self.adj_list[start][i] = (v, Graph.EdgesType.BACK)

    for s in self.adj_list:
      if not s in parent:
        parent[s] = -1
        cur_parent[s] = -1
        visit(s)

        parent = dict(itertools.chain(parent.items(), cur_parent.items()))

    print("Parent", parent)

  # O(E + V)
  def topological_sort(self):
    res = []
    cur_traversal_path = set()
    visited = set()

    def visit(start):
      for v, _ in self.adj_list[start]:
        if v in cur_traversal_path:
          raise Exception("Cyclic!")
        if not v in visited:
          cur_traversal_path.add(v)
          visit(v)
          cur_traversal_path.remove(v)

      visited.add(start)
      res.insert(0, start)

    for s in self.adj_list:
      if not s in visited:
        visit(s)

    return res