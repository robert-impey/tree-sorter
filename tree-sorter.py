#!/usr/bin/env python

import fileinput
import re

lines = []
for line in fileinput.input():
    lines.append(line.rstrip())

top_level = re.compile('^\w')
tree_separator = re.compile('^\s*$')
        
for line in lines:
    if top_level.match(line):
        print line
    elif tree_separator.match(line):
        print 
    else:
        pass
