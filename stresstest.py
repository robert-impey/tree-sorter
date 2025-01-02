#!/usr/bin/env python3

"""
Generate random tree lines and attempt to sort them.
Test that the output lines are in the correct order.
Repeat until failure or the process is killed.
"""

from treesorting import *
from randomtrees import *

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    add_simulation_args(parser)

    args = parser.parse_args()

    while True:
        random_tree_lines = generate_random_tree_lines(
            args.Depth,
            args.Items,
            args.Length,
            args.Alphabet)

        tree = lines_to_tree(random_tree_lines)

        lines = tree.get_lines()

        if not are_lines_sorted_tree(lines):
            print('A tree was not sorted correctly')

            print('Input')
            for line in random_tree_lines:
                print(line)

            print('Output')
            for line in lines:
                print(line)

            break
