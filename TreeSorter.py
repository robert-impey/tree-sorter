#!/usr/bin/env python

import fileinput
import re
from functools import total_ordering

def get_lines():
    lines = []
    for line in fileinput.input():
        lines.append(line.rstrip())
    return lines

def lines_to_tree(lines):
    tree = Tree()

    tree_stack = [tree]
    
    previous_indentation = ''
    
    leading_white_space_re = re.compile('^(\s*)(.+)')

    for line in lines:

        m = leading_white_space_re.match(line)
        if m:
            indentation = m.group(1)
            text = m.group(2)
            
            new_tree = Tree(text)

            parent_tree = tree_stack.pop()

            if len(indentation) < len(previous_indentation):
                pass
            elif len(indentation) > len(previous_indentation):
                tree_stack.append(parent_tree)
                tree_stack.append(new_tree)
            else:
                tree_stack.append(parent_tree)

            parent_tree.add_sub_tree(new_tree)

            previous_indentation = indentation

    return tree

@total_ordering
class Tree:
    def __init__(self, text = None):
        self.text = text
        self.sub_trees = []

    def get_text(self):
        return self.text
    
    def get_sub_trees(self):
        return sorted(self.sub_trees)

    def add_sub_tree(self, new_tree):
        return self.sub_trees.append(new_tree)

    def to_string(self, eol = "\n", indentation = '', tab = "\t"):
        if self.get_text() == None:
            current_text = ''
            current_indentation = ''
            tree_string = ''
        else:
            current_text = self.get_text()
            current_indentation = tab + indentation
            tree_string = current_indentation + current_text + eol
        
        for sub_tree in self.get_sub_trees():
            tree_string += sub_tree.to_string(indentation = current_indentation) 
        
        return tree_string

    def __eq__(self, other):
        return self.to_string() == other.to_string()

    def __lt__(self, other):
        return self.get_text() < other.get_text()

if __name__ == '__main__':
    lines = get_lines()

    tree = lines_to_tree(lines)
    
    print(tree.to_string()),
