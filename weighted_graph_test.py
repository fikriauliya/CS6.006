import unittest
from weighted_graph import *

class WeightedGraphTest(unittest.TestCase):
  def test_append_edge(self):
    g = WeightedGraph()

    g.append_edge('A', 'B', 19, False)
    g.append_edge('A', 'C', 7, False)
    g.append_edge('B', 'C', 11, False)
    g.append_edge('B', 'D', 4, False)
    g.append_edge('C', 'D', 15, False)
    g.append_edge('C', 'E', 5, False)
    g.append_edge('D', 'E', 13, False)

    g.print()

  def test_djikstra(self):
    g = WeightedGraph()

    g.append_edge('A', 'B', 19, False)
    g.append_edge('A', 'C', 7, False)
    g.append_edge('B', 'C', 11, False)
    g.append_edge('B', 'D', 4, False)
    g.append_edge('C', 'D', 15, False)
    g.append_edge('C', 'E', 5, False)
    g.append_edge('D', 'E', 13, False)

    g.print()
    parent, shortest_distances = g.djikstra('A')
    print(shortest_distances)
    print(parent)

    # {'A': 0, 'C': 7, 'B': 18, 'E': 12, 'D': 22}
    # {'A': -1, 'C': 'A', 'B': 'C', 'E': 'C', 'D': 'C'}
if __name__ == "__main__":
  unittest.main()