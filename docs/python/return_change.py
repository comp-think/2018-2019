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


# Test case for the algorithm
def test_return_change(amount, expected):
    result = return_change(amount)
    if expected == result:
        return True
    else:
        return False


# Code of the algorithm
def return_change(amount):
    result = {}
    coins = [2.0, 1.0, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01]

    for coin in coins:
        while float_diff(amount, coin) >= 0:
            amount = float_diff(amount, coin)

            if coin not in result:
                result[coin] = 0
            result[coin] = result[coin] + 1

    return result


def float_diff(f1, f2):
    return round(f1 - f2, 2)


change = 2.76
print(test_return_change(5.00, {2.0: 2, 1.0: 1}))
print(test_return_change(2.76, {2.0: 1, 0.5: 1, 0.2:1, 0.05:1, 0.01: 1}))


