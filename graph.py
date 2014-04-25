class Graph:
  adj_list = {}

  def __init__(self, graph_ascii = ''):
    edges = graph_ascii.split("\n")

    source_vertex_counter = 0
    for edge in edges:
      destination_vertex_counter = 0
      self.adj_list[source_vertex_counter] = set()
      for status in edge:
        if status == '1':
          self.adj_list[source_vertex_counter].add(destination_vertex_counter)
        destination_vertex_counter += 1
      source_vertex_counter += 1

  def print(self):
    for v1 in self.adj_list:
      print(v1, end="->")
      for v2 in self.adj_list[v1]:
        print(v2, end=" ")
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
        for adj_vertex in self.adj_list[frontier]:
          if not adj_vertex in level:
            level[adj_vertex] = cur_level
            parent[adj_vertex] = frontier
            next_frontiers.add(adj_vertex)

      frontiers = next_frontiers
      cur_level += 1

    return level

  def shortest_path(self, start, destination):
    level = self.bfs(start)
    if destination in level:
      return level[destination]
    else:
      return None