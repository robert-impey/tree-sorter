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
    blank_line = re.compile('^\s*$')
    tree = {}
    sub_tree = []

    cur_tree_name = None
    for line in lines:
        if top_level.match(line):
            if cur_tree_name != None:
                tree[cur_tree_name] = sorted(sub_tree)

            cur_tree_name = line
            sub_tree = []
        elif blank_line.match(line):
            pass
        else:
            sub_tree.append(line)

    if cur_tree_name != None:
        tree[cur_tree_name] = sorted(sub_tree)

    return tree

def tree_to_string(tree, eol = "\n"):
    tree_string = ''
    for key, val in sorted(tree.iteritems()):
        tree_string += key + eol
        for item in val:
            tree_string += item + eol
    return tree_string

if __name__ == '__main__':
    lines = get_lines()

    tree = parse_lines(lines)
    
    str = tree_to_string(tree)
    print str
