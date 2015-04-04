#!/usr/bin/env python

from TreeSorter import *
import unittest

class TestParsing(unittest.TestCase):
	def test_empty(self):
		lines = []
		tree = parse_lines(lines)
		self.assertEqual({}, tree)

		tree_string = tree_to_string(tree)
		self.assertEqual('', tree_string)
	
	def test_one_deep(self):
		lines = []
		lines.append('foo')
		lines.append("\tgaz")
		lines.append("\tbar")

		tree = parse_lines(lines)

		expected_tree_count = 1
		self.assertEqual(expected_tree_count, len(tree))

		tree_string = tree_to_string(tree)

		expected_string = """foo
	bar
	gaz
"""
		
		self.assertEqual(expected_string, tree_string)	

if __name__ == '__main__':
	unittest.main()
