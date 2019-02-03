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

from re import sub


def prepare(s):
    l = []

    support = ["9", "8", "7", "6", "5", "4", "3", "2", "1", "0"]

    for idx, c in enumerate(s):
        if c == "0" or c == "9":
            l.append(support[idx])
        else:
            l.append(c)

    return l


def s(l):
    list_r = list(range(len(l)))
    iters = list_r[1:]

    for iter in reversed(iters):
        for idx in range(iter):
            if l[idx] > l[idx + 1]:
                tmp = l[idx]
                l[idx] = l[idx + 1]
                l[idx + 1] = tmp

    return l


my_string_id = sub("\D", "", input("Please provide your matriculation number: "))
print("Result:", s(prepare(my_string_id)))
