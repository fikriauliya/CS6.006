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