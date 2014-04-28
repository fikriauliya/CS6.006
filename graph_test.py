from operator import methodcaller
import unittest
import operator
from graph import *

class GraphTest(unittest.TestCase):
  def test_graph_construction(self):
    g = Graph('100\n'
              '011\n'
              '001')
    g.print()

  def test_graph_bfs(self):
    g = Graph('1110\n'
              '0110\n'
              '0011\n'
              '1111')
    g.print()
    g.bfs()

  def test_shortest_path(self):
    g = Graph('11100\n'
              '01100\n'
              '00110\n'
              '11110\n'
              '00000')
    self.assertEqual(g.shortest_path(0, 0), 0)
    self.assertEqual(g.shortest_path(0, 1), 1)
    self.assertEqual(g.shortest_path(0, 2), 1)
    self.assertEqual(g.shortest_path(0, 3), 2)
    self.assertEqual(g.shortest_path(2, 3), 1)
    self.assertEqual(g.shortest_path(2, 1), 2)
    self.assertEqual(g.shortest_path(2, 4), None)

  def test_graph_dfs(self):
    g = Graph('11100\n'
              '01100\n'
              '00110\n'
              '11111\n'
              '00000')
    g.print()
    (parent, level) = g.dfs()
    print("Parent", parent)
    sorted_level = sorted(level.items(),key=operator.itemgetter(1))
    print("Level", sorted_level)

  def test_categorize_edges(self):
    g = Graph('010100\n'
              '000010\n'
              '000011\n'
              '010000\n'
              '000100\n'
              '000001')
    g.categorize_edges()
    g.print()

  def test_topological_sort(self):
    g = Graph('001\n'
              '100\n'
              '000')
    g.print()
    res = g.topological_sort()
    print(res)

if __name__ == "__main__":
  unittest.main()