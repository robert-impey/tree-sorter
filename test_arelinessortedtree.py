#!/usr/bin/env python3

from treesorting import *
import unittest


class TestEmpty(unittest.TestCase):
    def setUp(self):
        self.lines = []

    def test_empty_set_is_sorted(self):
        lines_are_sorted_tree = are_lines_sorted_tree(self.lines)
        self.assertTrue(lines_are_sorted_tree)


class TestSingleTree(unittest.TestCase):
    def setUp(self):
        self.lines = ['foo']

    def test_text(self):
        lines_are_sorted_tree = are_lines_sorted_tree(self.lines)
        self.assertTrue(lines_are_sorted_tree)
