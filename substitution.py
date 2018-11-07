#!/usr/bin/env python3

import random
from string import ascii_uppercase
from quote_file_mod import get_quote
def substitute(message):
    new_alphabet = {l1: l2 for l1, l2 in zip(ascii_uppercase,
                                             random.sample(ascii_uppercase, k=26))}
    return ''.join(new_alphabet.get(l, l) for l in message.upper())


if __name__ == '__main__':
    t = get_quote()
    #print(t)
    print(substitute(t))
