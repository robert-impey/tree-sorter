#!/usr/bin/env python

from TreeSorter import *
import unittest

class TestParsing(unittest.TestCase):
	def test_empty(self):
		lines = []
		tree = parse_lines(lines)
		self.assertEqual({}, tree)

if __name__ == '__main__':
	unittest.main()
