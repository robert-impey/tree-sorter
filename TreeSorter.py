#!/usr/bin/env python

import fileinput
import re

def get_lines():
    lines = []
    for line in fileinput.input():
        lines.append(line.rstrip())
    return lines

def parse_lines(lines):
    top_level = re.compile('^\w')
    tree_separator = re.compile('^\s*$')
    tree = {}
    
    for line in lines:
        if top_level.match(line):
            cur_tree_name = line
            cur_tree = []
        elif tree_separator.match(line):
            tree[cur_tree_name] = cur_tree
        else:
            cur_tree.append(line)
    
    return tree

def print_tree(tree):
    for key, val in sorted(tree.iteritems()):
        print key
        for item in val:
            print item
        print
    
if __name__ == '__main__':
    lines = get_lines()

    tree = parse_lines(lines)
    
    print_tree(tree)
