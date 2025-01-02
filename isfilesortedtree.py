#!/usr/bin/env python3

"""
Tells us if a tree file is in order.
"""

import argparse
from treesorting import is_file_sorted_tree

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('TreeFile',
                        help='The file containing the tree.')

    args = parser.parse_args()

    file_is_sorted = is_file_sorted_tree(args.TreeFile)

    print("Sorted" if file_is_sorted else "Not in order")
