import unittest
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
              '1111\n')
    g.print()
    g.bfs()

  def test_shortest_path(self):
    g = Graph('11100\n'
              '01100\n'
              '00110\n'
              '11110\n'
              '00000\n')
    self.assertEqual(g.shortest_path(0, 0), 0)
    self.assertEqual(g.shortest_path(0, 1), 1)
    self.assertEqual(g.shortest_path(0, 2), 1)
    self.assertEqual(g.shortest_path(0, 3), 2)
    self.assertEqual(g.shortest_path(2, 3), 1)
    self.assertEqual(g.shortest_path(2, 1), 2)
    self.assertEqual(g.shortest_path(2, 4), None)

