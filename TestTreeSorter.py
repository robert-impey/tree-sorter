#!/usr/bin/env python

from TreeSorter import *
import unittest

class TestEmpty(unittest.TestCase):
    def setUp(self):
        self.lines = []
        self.tree = lines_to_tree(self.lines)

    def test_tree(self):
        empty_tree = Tree()
        self.assertEqual(empty_tree, self.tree)

    def test_tree_text(self):
        expected_text = None
        self.assertEqual(expected_text, self.tree.get_text())

    def test_string(self):
        self.assertEqual('', self.tree.to_string())

class TestSingleTree(unittest.TestCase):
    def setUp(self):
        self.lines = ['foo']
        self.tree = lines_to_tree(self.lines)

    def test_text(self):
        expected_text = 'foo'
        self.assertEqual(expected_text, self.tree.get_text())

    def test_string(self):
        expected_string = "foo\n"
        self.assertEqual(expected_string, self.tree.to_string())

class TestOneDeep(unittest.TestCase):
    def setUp(self):
        self.lines = []
        self.lines.append("foo")
        self.lines.append("\tgaz")
        self.lines.append("\tbar")
        self.tree = lines_to_tree(self.lines)
    
    def test_tree_text(self):
        expected_text = 'foo'
        self.assertEqual(expected_text, self.tree.get_text())

    def test_tree_string(self):
        expected_string = "foo\n\tbar\n\tgaz"
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

class TestSorting(unittest.TestCase):
    def setUp(self):
        self.fruits = Tree('fruits')
        self.apple = Tree('apple')
        self.banana = Tree('banana')
        self.coconut = Tree('coconut')
   
    def assert_that_sub_trees_are_fruits_in_order(self, sub_trees):
        self.assertEqual('apple', sub_trees[0].get_text())
        self.assertEqual('banana', sub_trees[1].get_text())
        self.assertEqual('coconut', sub_trees[2].get_text())

    def test_adding_in_order(self):
        self.fruits.add_sub_tree(self.apple)
        self.fruits.add_sub_tree(self.banana)
        self.fruits.add_sub_tree(self.coconut)

        sub_trees = self.fruits.get_sub_trees()
        self.assert_that_sub_trees_are_fruits_in_order(sub_trees)

    def test_adding_out_of_order(self):
        self.fruits.add_sub_tree(self.banana)
        self.fruits.add_sub_tree(self.coconut)
        self.fruits.add_sub_tree(self.apple)

        sub_trees = self.fruits.get_sub_trees()
        self.assert_that_sub_trees_are_fruits_in_order(sub_trees)

if __name__ == '__main__':
    unittest.main()
