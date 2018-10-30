#!/usr/bin/env python3

from util import *
from random import randint

def get_alphabet(shift = 0):
    r = [n2l(l + shift) for l in range(0, 26)]
    return r


def caesar_cipher(message, shift, keep_spaces=True):
    return ''.join([l2n2ls(l,shift) # calculate the letter after shift
                    if l != ' ' # but only if the letter is not a space.
                    # if it is a space, insert a space or nothing, based on
                    # keep_spaces
                    else (' ' if keep_spaces else '')
                    for l in message]) # for each letter in message


if __name__ == '__main__':
    print(get_alphabet())
    print(get_alphabet(randint(0,25)))
    print('Hello World')
    print(caesar_cipher('Hello World', 7))
