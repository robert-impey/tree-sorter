#!/usr/bin/env python

import fileinput
import re

def get_lines():
    lines = []
    for line in fileinput.input():
        lines.append(line.rstrip())
    return lines

class Tree:
    def __init__(self, lines, indent = ''):
        self.lines = lines
        self.indent = indent

    def get_lines_until_same_indent(self):
        lines_at_current_indent = []
        
        indent_re = re.compile("^%s\s+" % self.indent)
        for line in self.lines[1:]:
            if indent_re.match(line):
                lines_at_current_indent.append(line)
            else:
                break
        
        return lines_at_current_indent

    def get_title(self):
        return self.lines[0].strip()

    def get_count(self):
        return 0

    def get_sub_trees(self):
        sub_trees = []
        previous_indent = self.indent
        leading_white_space_re = re.compile('^(\s*)')
        cur_sub_tree_lines = []
        for line in self.get_lines_until_same_indent():
            current_indent = leading_white_space_re.search(line).group(0)

            if len(previous_indent) == len(current_indent):
                cur_sub_tree_lines.append(lines)
            else:
                sub_trees.append(Tree(cur_sub_tree_lines))

            previous_indent = current_indent
        
        sub_trees.append(Tree(cur_sub_tree_lines))

        return sub_trees

    def to_string(self, eol = "\n"):
        tree_string = self.get_title() + eol
        for sub_tree in self.get_sub_trees():
            tree_string += sub_tree.to_string() 
        return tree_string

if __name__ == '__main__':
    lines = get_lines()

    tree = Tree(lines)
    
    print tree.to_string()
