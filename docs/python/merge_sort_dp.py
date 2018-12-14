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


# Import the function 'merge' from the module 'merge' (file 'merge.py')
from merge import merge


# Test case for the algorithm
def test_merge_sort_dp(input_list, expected):
    result = merge_sort_dp(input_list)
    if expected == result:
        return True
    else:
        return False


# Code of the algorithm
def merge_sort_dp(input_list, prev_l=list()):
    result = find_solution(input_list, prev_l)

    if result is None:
        if len(input_list) <= 1:
            result = input_list
            store_solution(result, prev_l)
        else:
            input_list_len = len(input_list)
            mid = input_list_len // 2

            left = merge_sort_dp(input_list[0:mid], prev_l)
            right = merge_sort_dp(input_list[mid:input_list_len], prev_l)
            result = merge(left, right)
            store_solution(result, prev_l)
    return result


def find_solution(input_list, sol_list):
    input_dic = create_list_dict(input_list)
    for d, sol in sol_list:
        if input_dic == d:
            return list(sol)


def store_solution(input_list, solution_list):
    d = create_list_dict(input_list)
    solution_list.append((d, list(input_list)))


def create_list_dict(input_list):
    d = {}
    for el in input_list:
        if el not in d:
            d[el] = 0
        d[el] = d[el] + 1
    return d


print(test_merge_sort_dp([], []))
print(test_merge_sort_dp([1], [1]))
print(test_merge_sort_dp([3, 4, 1, 2, 9, 8, 2], [1, 2, 2, 3, 4, 8, 9]))
print(test_merge_sort_dp(["Coraline", "American Gods", "The Graveyard Book", "Good Omens", "Neverwhere"],
                         ["American Gods", "Coraline", "Good Omens", "Neverwhere", "The Graveyard Book"]))
print(test_merge_sort_dp(["Coraline", "American Gods", "The Graveyard Book", "Good Omens", "Neverwhere", "American Gods",
                          "American Gods", "Good Omens", "The Graveyard Book", "American Gods", "Neverwhere", "Coraline"],
                         ["American Gods", "American Gods","American Gods", "American Gods", "Coraline", "Coraline",
                          "Good Omens", "Good Omens", "Neverwhere",  "Neverwhere", "The Graveyard Book", "The Graveyard Book"]))
