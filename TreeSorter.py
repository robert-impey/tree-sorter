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
    
    cur_tree_name = None
    for line in lines:
        if top_level.match(line):
            if cur_tree_name != None:
                tree[cur_tree_name] = sub_tree

            cur_tree_name = line
            sub_tree = []
        elif blank_line.match(line):
            pass
        else:
            sub_tree.append(line)
    
    return tree

def tree_to_string(tree, eol = "\n"):
    str = ''
    for key, val in sorted(tree.iteritems()):
        str += key + eol
        for item in val:
            str += item + eol
    return str

if __name__ == '__main__':
    lines = get_lines()

    tree = parse_lines(lines)
    
    str = tree_to_string(tree)
    print str
