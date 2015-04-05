#!/usr/bin/env python

from TreeSorter import *
import unittest

class TestParsingEmpty(unittest.TestCase):
	def setUp(self):
		self.lines = []
		self.tree = parse_lines(self.lines)
		self.tree_string = tree_to_string(self.tree)

	def test_tree(self):
		self.assertEqual({}, self.tree)
	
	def test_string(self):
		self.assertEqual('', self.tree_string)
	
class TestOneDeep(unittest.TestCase):
	def setUp(self):
		self.lines = []
		self.lines.append('foo')
		self.lines.append("\tgaz")
		self.lines.append("\tbar")
		self.tree = parse_lines(self.lines)
		self.tree_string = tree_to_string(self.tree)

	def test_tree_count(self):
		expected_tree_count = 1
		self.assertEqual(expected_tree_count, len(self.tree))

	def test_tree_string(self):
		expected_string = """foo
	bar
	gaz
"""
		
		self.assertEqual(expected_string, self.tree_string)

if __name__ == '__main__':
	unittest.main()
