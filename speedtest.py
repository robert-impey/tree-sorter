#!/usr/bin/env python3

"""
Generate random trees and sort them.
Time the sorting part.
Print statistics on the times.
"""

import argparse
import time
from statistics import mean

from randomtrees import add_simulation_args, generate_random_tree_lines_from_args
from treesorting import lines_to_tree

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    add_simulation_args(parser)

    parser.add_argument('--Iterations',
                        help='The number of iterations.',
                        type=int,
                        default=100)

    args = parser.parse_args()

    remaining_iterations = args.Iterations

    times = []
    while remaining_iterations > 0:
        remaining_iterations -= 1

        random_tree_lines = generate_random_tree_lines_from_args(args)

        start = time.process_time()

        tree = lines_to_tree(random_tree_lines)

        tree.get_lines()

        stop = time.process_time()

        times.append(stop - start)

    print(f"Number of times: {len(times)}")
    print(f"Min time: {min(times)} s")
    print(f"Max time: {max(times)} s")
    print(f"Mean time: {mean(times)} s")
