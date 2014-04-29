import operator
import itertools
import sys
import heapq

class WeightedGraph:
  def __init__(self, graph_ascii = ''):
    self.adj_list = dict()
    self.reversed_adj_list = dict()

  def print(self):
    for v1 in self.adj_list:
      print(v1, end = " -> ")
      for v2 in self.adj_list[v1]:
        print(v2, end = " ")
      print()

  def append_edge(self, source_vertex, destination_vertex, weight, directed = True):
    if not source_vertex in self.adj_list:
      self.adj_list[source_vertex] = []

    if not destination_vertex in self.reversed_adj_list:
      self.reversed_adj_list[destination_vertex] = []

    self.adj_list[source_vertex].append((destination_vertex, weight))
    self.reversed_adj_list[destination_vertex].append((source_vertex, weight))

    if not directed:
      if not destination_vertex in self.adj_list:
        self.adj_list[destination_vertex] = []
      if not source_vertex in self.reversed_adj_list:
        self.reversed_adj_list[source_vertex] = []

      self.adj_list[destination_vertex].append((source_vertex, weight))
      self.reversed_adj_list[source_vertex].append((destination_vertex, weight))

  # Single source shortest path
  # O(V lg V + E lg V)
  # Using Fibonacci heap: O(V lg V + E)
  def djikstra(self, start):
    frontier = [(0, start)] # (weight, vertex)

    parent = {v:-1 for v in self.adj_list.keys()}
    distances = {v:sys.maxsize for v in self.adj_list.keys()}
    distances[start] = 0
    found = set()

    while frontier:
      (shortest_weight, shortest_vertex) = heapq.heappop(frontier)

      if not shortest_vertex in found:
        found.add(shortest_vertex)

        for v, w in self.adj_list[shortest_vertex]:
          if shortest_weight + w < distances[v]:
            distances[v] = shortest_weight + w
            parent[v] = shortest_vertex
            heapq.heappush(frontier, (distances[v], v))

    return (parent, distances)

  # Single source shortest path, allow negative weight but not negative cycle
  # O(|V| |E|)
  def bellman_ford(self, start):
    distance = {v:sys.maxsize for v in self.adj_list.keys()}
    parent = {v:-1 for v in self.adj_list.keys()}
    distance[start] = 0

    for i in range(len(self.adj_list.keys()) - 1):
      # For each edges
      for v1 in self.adj_list:
        for v2, w in self.adj_list[v1]:
          if distance[v1] + w < distance[v2]:
            parent[v2] = v1
            distance[v2] = distance[v1] + w

    # Check for cycle
    for v1 in self.adj_list:
      for v2, w in self.adj_list[v1]:
        if distance[v1] + w < distance[v2]:
          raise Exception("Cycle detected")

    return (parent, distance)

  def bellman_form_memoization(self, start):
    vertex_count = len(self.adj_list.keys())
    distance_memo = {v:[None for k in range(vertex_count)] for v in self.adj_list.keys()}
    parent = {v:-1 for v in self.adj_list.keys()}

    def rec(k, target):
      if k <= 0: return sys.maxsize
      if distance_memo[target][k] != None: return distance_memo[target][k]
      res = 0

      if target == start:
        res = 0
      else:
        min_dist = sys.maxsize
        for v, w in self.reversed_adj_list[target]:
          dist = rec(k - 1, v) + w
          if dist < min_dist:
            min_dist = dist
            parent[target] = v

        res = min_dist

      distance_memo[target][k] = res
      return res

    distance = {}
    for target in self.adj_list.keys():
      distance[target] = rec(vertex_count - 1, target)
    return (parent, distance)

  def djikstre_single_target(self, start, target):
    frontiers = [(0, start)]

    parent = {v:-1 for v in self.adj_list}
    distance = {v:sys.maxsize for v in self.adj_list}
    distance[start] = 0
    found = set()

    while frontiers:
      smallest_distance, smallest_vertex = heapq.heappop(frontiers)

      if not smallest_vertex in found:
        found.add(smallest_vertex)
        if smallest_vertex == target:
          return (parent, distance)

        for v, w in self.adj_list[smallest_vertex]:
          if smallest_distance + w < distance[v]:
            distance[v] = smallest_distance + w
            parent[v] = smallest_vertex
            heapq.heappush(frontiers, (distance[v], v))

    return (parent, distance)

  def djikstra_bidirection(self, start, target):
    # TODO
    pass