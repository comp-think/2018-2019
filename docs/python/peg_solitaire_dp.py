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

from anytree import Node
from collections import deque
from peg_solitaire import create_6x6_square_board, valid_moves, apply_move, undo_move


# Test case for the algorithm
def test_solve(pegs, holes, expected):
    result = solve(pegs, holes)
    if expected == result.name["in"] and len(pegs) == 1:
        return True
    else:
        return False


# Code of the algorithm
def solve(pegs, holes, last_move=Node("start"), no_win=list()):
    result = None

    if pegs not in no_win:
        no_win.append(set(pegs))

        if len(pegs) == 1 and (3, 2) in pegs:  # leaf-win base case
            result = last_move
        else:
            last_move.children = valid_moves(pegs, holes)

            if len(last_move.children) == 0:  # leaf-lose base case
                undo_move(last_move, pegs, holes)  # backtracking
            else:  # recursive step
                possible_moves = deque(last_move.children)

                while result is None and len(possible_moves) > 0:
                    current_move = possible_moves.pop()
                    apply_move(current_move, pegs, holes)
                    result = solve(pegs, holes, current_move, no_win)

                if result is None:
                    undo_move(last_move, pegs, holes)  # backtracking
    else:
        undo_move(last_move, pegs, holes)  # backtracking

    return result


pegs, holes = create_6x6_square_board()
print(test_solve(pegs, holes, (3, 2)))
