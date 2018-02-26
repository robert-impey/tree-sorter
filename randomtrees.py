#!/usr/bin/env python3

import random

"""
Generates random trees
"""

import argparse

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"

def generate_random_item(length=8, chars=alphabet):
    item = ""

    for i in range(length):
        index = random.randint(0, len(chars) - 1)

        item += chars[index]

    return item


def generate_random_tree_lines(
        depth,
        items,
        length,
        chars=alphabet,
        current_indentation=''):
    lines = []

    if depth > 0:
        remaining_items_to_add = items

        while remaining_items_to_add > 0:
            lines.append('{0}{1}'.format(current_indentation, generate_random_item(length, chars)))

            remaining_items_to_add -= 1
            sub_lines = generate_random_tree_lines(
                depth - 1,
                items,
                length,
                chars,
                current_indentation + '    ')
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
    parser.add_argument('--Length',
                        help='The length of each item.',
                        type=int,
                        default=8)
    parser.add_argument('--Alphabet',
                        help='The alphabet of allowed characters.',
                        type=str,
                        default=alphabet)

    args = parser.parse_args()

    random_tree_lines = generate_random_tree_lines(
        args.Depth,
        args.Items,
        args.Length,
        args.Alphabet)

    for line in random_tree_lines:
        print(line)
