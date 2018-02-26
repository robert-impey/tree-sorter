#!/usr/bin/env python3

import argparse
import shutil
from treesorting import *


if __name__ == '__main__':
    parser = argparse.ArgumentParser('Sort trees')

    parser.add_argument('TreeFile',
                        help='The file containing the tree.')
    parser.add_argument('--SeparateTopLevel',
                        help='Separate top level trees with a blank line.',
                        action='store_true')
    parser.add_argument('--InPlace',
                        help='Write the output on top of the input file.',
                        action='store_true')

    args = parser.parse_args()

    file_name = args.TreeFile
    separate_top_level = args.SeparateTopLevel
    in_place = args.InPlace

    lines = get_lines(file_name)

    if in_place and are_lines_sorted_tree(lines):
        print('In place sorting requested but already sorted.')
    else:
        if in_place:
            backup = '{0}.bak'.format(file_name)
            shutil.copy2(file_name, backup)

        tree = lines_to_tree(lines)

        output = tree.to_string(separate_top_level=separate_top_level)
        if in_place:
            with open(file_name, 'w') as output_file:
                output_file.write(output)
        else:
            print(output, end=' ')
