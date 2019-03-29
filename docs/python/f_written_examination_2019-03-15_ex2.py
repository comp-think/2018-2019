# -*- coding: utf-8 -*-
# Copyright (c) 2019, Silvio Peroni <essepuntato@gmail.com>
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

from collections import deque


def f(fn, mn):
    l = deque()
    digits = []

    for i in range(len(fn)):
        j = i % len(mn)
        digits.append(int(mn[len(mn) - 1 - j]))

    for idx, d in enumerate(reversed(digits)):
        if idx < (len(digits) / 2):
            l.append((d, digits[idx]))

    result = []
    for c in fn:
        result.append(c)

    while l:
        t = l.pop()
        if t[0] < len(fn) and t[1] < len(fn):
            tmp = fn[t[0]]
            result[t[0]] = fn[t[1]]
            result[t[1]] = tmp

    return "".join(result)


my_fn = input("Please provide your family name: ").strip()
my_mn = input("Please provide your matriculation number: ").strip()
print("Result:", f(my_fn, my_mn))
