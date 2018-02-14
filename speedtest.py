#!/usr/bin/env python3

"""
Generate random trees and sort them.
Time the sorting part.
Print statistics on the times.
"""

import time
from statistics import mean

from randomtrees import *
from treesorting import *

if __name__ == '__main__':
    parser = argparse.ArgumentParser('Tree sorting Stress Test')

    parser.add_argument('--Iterations',
                        help='The number of iterations.',
                        type=int,
                        default=100)
    parser.add_argument('--Depth',
                        help='The depth of the trees.',
                        type=int,
                        default=3)
    parser.add_argument('--Items',
                        help='The number of items for each node of the tree.',
                        type=int,
                        default=10)

    args = parser.parse_args()

    remaining_iterations = args.Iterations

    times = []
    while remaining_iterations > 0:
        remaining_iterations -= 1

        random_tree_lines = generate_random_tree_lines(args.Depth, args.Items)

        start = time.process_time()

        tree = lines_to_tree(random_tree_lines)

        tree.get_lines()

        stop = time.process_time()

        times.append(stop - start)

    print("Number of times: {0}".format(len(times)))
    print("Min time: {0} s".format(min(times)))
    print("Max time: {0} s".format(max(times)))
    print("Mean time: {0} s".format(mean(times)))
