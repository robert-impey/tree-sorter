#!/usr/bin/env python

import fileinput
import re

lines = []
for line in fileinput.input():
    lines.append(line.rstrip())

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

for key, val in sorted(tree.iteritems()):
    print key
    for item in val:
        print item
    print

