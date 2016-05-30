#!/usr/bin/env python3

import argparse
import re
import shutil
from functools import total_ordering

indentation_chars = 4


def get_lines(file_name):
    lines = []

    with open(file_name) as in_file:
        for line in in_file:
            line = line.rstrip()
            if len(line) > 0:
                lines.append(line)

    return lines


def lines_to_tree(lines):
    root = Tree()

    tree_stack = [(root, 0)]

    leading_white_space_re = re.compile('^(\s*)(.*)')

    for line in lines:
        m = leading_white_space_re.match(line)
        if m:
            indentation = m.group(1)
            text = m.group(2).rstrip()

            new_tree = Tree(text)

            current_depth = len(indentation)

            while tree_stack:
                (popped_tree, popped_child_depth) = tree_stack.pop()
                if current_depth == popped_child_depth:
                    parent_tree = popped_tree
                    parent_child_depth = popped_child_depth
                    break
                else:
                    popped_tree.finalise()

            parent_tree.add_sub_tree(new_tree)
            tree_stack.append((parent_tree, parent_child_depth))

            child_depth = current_depth + indentation_chars

            tree_stack.append((new_tree, child_depth))

    for (tree, _) in tree_stack:
        tree.finalise()

    return root


@total_ordering
class Tree:
    def __init__(self, text=None):
        self.text = text
        self.sub_trees = []

    def get_text(self):
        return self.text

    def finalise(self):
        self.sub_trees.sort()

    def get_sub_trees(self):
        return self.sub_trees

    def add_sub_tree(self, new_tree):
        return self.sub_trees.append(new_tree)  # Why not insert in order?

    def is_top_level(self):
        return self.text is None

    def to_string(self, eol="\n", indentation='',
                  tab="    ", separate_top_level=False):
        if self.is_top_level():
            child_indentation = ''
            tree_string = ''
            post_tree_new_line = separate_top_level
        else:
            current_text = self.get_text()
            tree_string = indentation + current_text + eol
            child_indentation = indentation + tab
            post_tree_new_line = False

        first = True
        for sub_tree in self.get_sub_trees():
            if first:
                first = False
            else:
                if post_tree_new_line:
                    tree_string += eol

            tree_string += sub_tree.to_string(
                indentation=child_indentation,
                eol=eol, tab=tab,
                separate_top_level=separate_top_level)

        return tree_string

    def __str__(self):
        if self.get_text() is None:
            return '"No Text"'
        return self.get_text()

    def __eq__(self, other):
        if other is None:
            return False

        if self.text != other.text:
            return False

        return self.to_string() == other.to_string()

    def __lt__(self, other):
        if self.text is not None and other.text is not None:
            if self.text < other.text:
                return True

        return self.to_string() < other.to_string()


if __name__ == '__main__':
    parser = argparse.ArgumentParser('Sort trees')

    parser.add_argument('TreeFile',
                        help='The file containing the tree.')
    parser.add_argument('--SeparateTopLevel',
                        help='Separate top level trees with a blank line.',
                        action='store_true')
    parser.add_argument('--InPlace',
                        help='Write the output on top of the input file.',
                        action='store_true')

    args = parser.parse_args()

    file_name = args.TreeFile
    separate_top_level = args.SeparateTopLevel
    in_place = args.InPlace

    if in_place:
        backup = '{0}.bak'.format(file_name)
        shutil.copy2(file_name, backup)

    lines = get_lines(file_name)

    tree = lines_to_tree(lines)

    output = tree.to_string(separate_top_level=separate_top_level)
    if in_place:
        with open(file_name, 'w') as output_file:
            output_file.write(output)
    else:
        print(output, end=' ')
