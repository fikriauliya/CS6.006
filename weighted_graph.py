import operator
import itertools
import sys
import heapq

class WeightedGraph:
  def __init__(self, graph_ascii = ''):
    self.adj_list = dict()

  def print(self):
    for v1 in self.adj_list:
      print(v1, end = " -> ")
      for v2 in self.adj_list[v1]:
        print(v2, end = " ")
      print()

  def append_edge(self, source_vertex, destination_vertex, weight, directed = True):
    if not source_vertex in self.adj_list:
      self.adj_list[source_vertex] = []

    self.adj_list[source_vertex].append((destination_vertex, weight))
    if not directed:
      if not destination_vertex in self.adj_list:
        self.adj_list[destination_vertex] = []

      self.adj_list[destination_vertex].append((source_vertex, weight))

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