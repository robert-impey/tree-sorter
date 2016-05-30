#!/usr/bin/env python3

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
        expected_text = None
        self.assertEqual(expected_text, self.tree.get_text())

    def test_string(self):
        expected_string = "foo\n"
        self.assertEqual(expected_string, self.tree.to_string())


class TestOneDeep(unittest.TestCase):
    def setUp(self):
        self.lines = []
        self.lines.append("foo")
        self.lines.append("    gaz")
        self.lines.append("    bar")
        self.tree = lines_to_tree(self.lines)

    def test_tree_text(self):
        """The root tree should not have any text."""
        expected_text = None
        self.assertEqual(expected_text, self.tree.get_text())

    def test_tree_string(self):
        expected_string = "foo\n    bar\n    gaz\n"
        self.assertEqual(expected_string, self.tree.to_string())


class TestTwoTreesOneDeep(unittest.TestCase):
    def setUp(self):
        self.lines = []
        self.lines.append('2')
        self.lines.append("    2")
        self.lines.append("    1")
        self.lines.append('1')
        self.lines.append("    2")
        self.lines.append("    1")
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
        self.tree = lines_to_tree(self.lines)
        self.tree_string = self.tree.to_string()

    def test_two_deep_tree_string(self):
        expected_string = """A
    Aa
        A1
        A2
    Ab
        A1
        A2
B
    Ba
        B1
        B2
    Bb
        B1
        B2
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

        self.fruits.finalise()

        sub_trees = self.fruits.get_sub_trees()
        self.assert_that_sub_trees_are_fruits_in_order(sub_trees)


class TestTreesInFiles(unittest.TestCase):
    def setUp(self):
        with open('fixtures/two-deep.txt') as target_file:
            self.target = target_file.read()
        self.two_deep_unsorted = lines_to_tree(get_lines('fixtures/two-deep-unsorted.txt'))

    def test_remove_gaps(self):
        self.assertEqual(self.two_deep_unsorted.to_string(), self.target)


class TestTreesSeparatedByGaps(unittest.TestCase):
    def setUp(self):
        with open('fixtures/two-deep.txt') as target_file:
            self.target = target_file.read()
        self.two_deep_with_gaps = lines_to_tree(get_lines('fixtures/two-deep-with-gaps.txt'))

    def test_remove_gaps_from_files(self):
        self.assertEqual(self.two_deep_with_gaps.to_string(), self.target)


class TestTreesWithDuplicates(unittest.TestCase):
    def setUp(self):
        with open('fixtures/two-deep-with-duplicates.txt') as target_file:
            self.target = target_file.read()
        self.two_deep_unsorted = lines_to_tree(get_lines('fixtures/two-deep-with-duplicates-unsorted.txt'))

    def test_sort_with_duplicates(self):
        self.assertEqual(self.two_deep_unsorted.to_string(), self.target)


class TestTreesOutputWithGaps(unittest.TestCase):
    def setUp(self):
        with open('fixtures/two-deep-with-gaps-sorted.txt') as target_file:
            self.target = target_file.read()
        self.two_deep_unsorted = lines_to_tree(get_lines('fixtures/two-deep-with-gaps.txt'))

    def test_sort_and_separate(self):
        self.assertEqual(self.two_deep_unsorted.to_string(separate_top_level=True), self.target)


if __name__ == '__main__':
    unittest.main()
