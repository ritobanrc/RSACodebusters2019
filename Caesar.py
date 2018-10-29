#!/usr/bin/env python3

from util import *
from random import randint

def get_alphabet(shift = 0):
    r = [n2l(l + shift) for l in range(0, 26)]
    return r


def caesar_cipher(message, shift, keep_spaces=True):
    return ''.join([n2l(l2n(l) + shift) if l != ' ' else (' ' if keep_spaces
                                                          else '') for l in message.upper()])


if __name__ == '__main__':
    print(get_alphabet())
    print(get_alphabet(randint(0,25)))
    print(caesar_cipher('Hello World', 7))
