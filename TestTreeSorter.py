#!/usr/bin/env python

from TreeSorter import *
import unittest

class TestEmpty(unittest.TestCase):
	def setUp(self):
		self.lines = []
		self.tree = lines_to_tree(self.lines)

	def test_tree(self):
		self.assertEqual({}, self.tree)

	def test_tree_text(self):
		expected_text = None
		self.assertEqual(expected_text, self.tree.get_text())

	def test_string(self):
		self.assertEqual('', self.tree.to_string())
	
class TestOneDeep(unittest.TestCase):
	def setUp(self):
		self.lines = []
		self.lines.append('foo')
		self.lines.append("\tgaz")
		self.lines.append("\tbar")
		self.tree = lines_to_tree(self.lines)
	
	def test_tree_text(self):
		expected_text = 'foo'
		self.assertEqual(expected_text, self.tree.get_text())

	def test_tree_string(self):
		expected_string = """foo
	bar
	gaz
"""
		self.assertEqual(expected_string, self.tree.to_string())

class TestTwoTreesOneDeep(unittest.TestCase):
	def setUp(self):
		self.lines = []
		self.lines.append('2')
		self.lines.append("\t2")
		self.lines.append("\t1")
		self.lines.append('1')
		self.lines.append("\t2")
		self.lines.append("\t1")
		self.tree = lines_to_tree(self.lines)

	def test_tree_string(self):
		expected_string = """1
	1
	2
2
	1
	2
"""
		self.assertEqual(expected_string, self.tree.to_string())

class TestTwoDeep(unittest.TestCase):
	def setUp(self):
		self.lines = []
		self.lines.append('A')
		self.lines.append("\tb")
		self.lines.append("\t\t2")
		self.lines.append("\t\t1")
		self.lines.append("\ta")
		self.lines.append("\t\t2")
		self.lines.append("\t\t1")
		self.tree = lines_to_tree(self.lines)
		self.tree_string = self.tree.to_string()

	def test_tree_string(self):
		expected_string = """A
	a
		1
		2
	b
		1
		2
"""
		self.assertEqual(expected_string, self.tree.to_string())

if __name__ == '__main__':
	unittest.main()
