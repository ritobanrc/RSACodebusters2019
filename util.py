#!/bin/python3

def n2l(n):
    return chr((n%26)+65)

def l2n(l):
    return (ord(l)-65) % 26


if __name__ == '__main__':
    print('A: ', n2l(0))
    print('N: ', n2l(13))
    print('23: ', l2n('X'))
    print('1: ', l2n('B'))
