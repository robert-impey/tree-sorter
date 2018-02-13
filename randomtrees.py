import random


def generate_random_tree_lines(depth, items, current_indentation=''):
    lines = ['{0}{1}'.format(current_indentation, random.random())]

    if depth >= 0:

        remaining_items_to_add = items

        while remaining_items_to_add >= 0:
            remaining_items_to_add -= 1
            sub_lines = generate_random_tree_lines(depth - 1, items, current_indentation + '    ')
            for sub_line in sub_lines:
                lines.append(sub_line)

    return lines
