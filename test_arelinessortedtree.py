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


class TestOneDeepInOrder(unittest.TestCase):
    def setUp(self):
        self.lines = []
        self.lines.append("foo")
        self.lines.append("    bar")
        self.lines.append("    gaz")

    def test_assessment(self):
        self.assertTrue(are_lines_sorted_tree(self.lines))


class TestOneDeepOutOfOrder(unittest.TestCase):
    def setUp(self):
        self.lines = []
        self.lines.append("foo")
        self.lines.append("    gaz")
        self.lines.append("    bar")

    def test_assessment(self):
        self.assertFalse(are_lines_sorted_tree(self.lines))


class TestTwoDeepInOrder(unittest.TestCase):
    def setUp(self):
        self.lines = []
        self.lines.append('A')
        self.lines.append("    Aa")
        self.lines.append("        A1")
        self.lines.append("        A2")
        self.lines.append("    Ab")
        self.lines.append("        A1")
        self.lines.append("        A2")
        self.lines.append('B')
        self.lines.append("    Ba")
        self.lines.append("        B1")
        self.lines.append("        B2")
        self.lines.append("    Bb")
        self.lines.append("        B1")
        self.lines.append("        B2")

    def test_assessment(self):
        self.assertTrue(are_lines_sorted_tree(self.lines))


class TestTwoDeepOutOfOrder(unittest.TestCase):
    def setUp(self):
        self.lines = []
        self.lines.append('A')
        self.lines.append("    Ab")
        self.lines.append("        A2")
        self.lines.append("        A1")
        self.lines.append("    Aa")
        self.lines.append("        A2")
        self.lines.append("        A1")
        self.lines.append('B')
        self.lines.append("    Bb")
        self.lines.append("        B2")
        self.lines.append("        B1")
        self.lines.append("    Ba")
        self.lines.append("        B2")
        self.lines.append("        B1")

    def test_assessment(self):
        self.assertFalse(are_lines_sorted_tree(self.lines))


class TestTreeFilesWithGapsInOrder(unittest.TestCase):
    def test_assessment(self):
        self.assertTrue(is_file_sorted_tree('fixtures/two-deep-with-gaps-sorted.txt'))


class TestTreeFilesWithGapsOutOfOrder(unittest.TestCase):
    def test_assessment(self):
        self.assertFalse(is_file_sorted_tree('fixtures/two-deep-with-gaps.txt'))


class TestTreeFilesInOrderAfterDrop(unittest.TestCase):
    def test_assessment(self):
        self.assertTrue(is_file_sorted_tree('fixtures/in-order-after-depth-drop.txt'))


class TestTreeFilesOutOfOrderAfterDrop(unittest.TestCase):
    def test_assessment(self):
        self.assertFalse(is_file_sorted_tree('fixtures/out-of-order-after-depth-drop.txt'))
