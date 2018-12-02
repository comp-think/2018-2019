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


from re import findall


# This simple functions has been developed to test the answers provided by students to the
# exercise number 3 of the first partial examination held on the 28th of November 2018.
# It takes in input the digits of the matriculation number, the rules of the machine, and
# the number of iterations after which the machine should stop, and returns the value of the
# 10 digits (appropriately converted in 0-1 symbols) after the execution of the machine.
def turing_machine(digits, rules, iterations):
    tape = [str(int(n) % 2) for n in list(digits)]
    l_digits = len(digits)
    head = l_digits - 1
    state = rules["start"]
    past_iterations = 0

    run = True
    while run:
        if past_iterations > iterations:
            run = False
        else:
            past_iterations += 1

            read_symbol = tape[head] if 0 <= head < l_digits else "0"
            rule = rules[state][read_symbol]

            if rule is None:
                run = False
            else:
                if 0 <= head < l_digits:
                    tape[head] = rule["write"]
                head += -1 if rule["left"] else 1
                state = rule["next"]

    return "".join(tape)


rules = {
    "start": "A",
    "A": {
        "0": {"write": "0", "left": True, "next": "A"},
        "1": {"write": "0", "left": True, "next": "B"}
    },
    "B": {
        "0": {"write": "1", "left": False, "next": "B"},
        "1": {"write": "1", "left": True, "next": "C"}
    },
    "C": {  # stop state
        "0": None,
        "1": None
    }
}

matriculation_number = "".join(findall("\d", input("Please provide your matriculation number: ")))
print("Result:", turing_machine(matriculation_number, rules, 50))
