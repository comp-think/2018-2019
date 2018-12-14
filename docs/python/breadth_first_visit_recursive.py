# -*- coding: utf-8 -*-
# Copyright (c) 2018, Silvio Peroni <essepuntato@gmail.com>
#
# Permission to use, copy, modify, and/or distribute this software for any purpose
# with or without fee is hereby granted, provided that the above copyright notice
# and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH
# REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND
# FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT, INDIRECT,
# OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE,
# DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS
# ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS
# SOFTWARE.

from tree_instructions import *


# Test case for the algorithm
def test_breadth_first_visit_recursive(root_node, expected):
    result = breadth_first_visit_recursive(root_node)
    if expected == result:
        return True
    else:
        return False


# Code of the algorithm
def breadth_first_visit_recursive(root_node):
    n_ancestors = len(root_node.ancestors)

    if n_ancestors == 0:
        cur_node = root_node
        levels = {}
    else:
        cur_node = root_node[0]
        levels = root_node[1]

    max_level = n_ancestors
    add_to_level(cur_node, n_ancestors, levels)

    for child in cur_node.children:
        cur_level = breadth_first_visit_recursive((child, levels))
        if cur_level > max_level:
            max_level = cur_level

    if n_ancestors:
        return max_level
    else:
        result = []
        for level in range(max_level + 1):
            result.extend(levels[level])
        return result


def add_to_level(node, level, levels):
    if level not in levels:
        levels[level] = []
    levels[level].append(node)


bfv = [book,
       chapter_1, chapter_2, text_8,
       paragraph_1, paragraph_2, paragraph_3, text_7,
       text_1, quotation_1, text_3, quotation_2, text_5, text_6,
       text_2, text_4]
print(test_breadth_first_visit_recursive(book, bfv))