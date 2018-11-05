#!/usr/bin/env python3

import random
from string import ascii_uppercase

def substitute(message):
    new_alphabet = {l1: l2 for l1, l2 in zip(ascii_uppercase,
                                             random.sample(ascii_uppercase, k=26))}
    return ''.join(new_alphabet.get(l, l) for l in message.upper())


if __name__ == '__main__':
    print(substitute('The quick brown fox jumps over the lazy dog.'))
