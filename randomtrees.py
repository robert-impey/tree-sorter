import random

"""
Generates random trees
"""

import argparse


def generate_random_item(length=8, chars="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"):
    item = ""

    for i in range(length):
        index = random.randint(0, len(chars) - 1)

        item += chars[index]

    return item


def generate_random_tree_lines(depth, items, current_indentation=''):
    lines = []

    if depth > 0:
        remaining_items_to_add = items

        while remaining_items_to_add > 0:
            lines.append('{0}{1}'.format(current_indentation, generate_random_item()))

            remaining_items_to_add -= 1
            sub_lines = generate_random_tree_lines(depth - 1, items, current_indentation + '    ')
            for sub_line in sub_lines:
                lines.append(sub_line)

    return lines


if __name__ == '__main__':
    parser = argparse.ArgumentParser('Tree sorting Stress Test')

    parser.add_argument('--Depth',
                        help='The depth of the trees.',
                        type=int,
                        default=3)
    parser.add_argument('--Items',
                        help='The number of items for each node of the tree.',
                        type=int,
                        default=10)

    args = parser.parse_args()

    random_tree_lines = generate_random_tree_lines(args.Depth, args.Items)

    for line in random_tree_lines:
        print(line)
