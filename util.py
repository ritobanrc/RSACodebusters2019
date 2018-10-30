#!/bin/python3

def n2l(n):
    return chr((n%26)+65)

def l2n(l):
    if l.isupper():
        return (ord(l)-65) % 26
    else:
        return (ord(l)-97) % 26

def l2n2ls(l,s=0):
    if l.isupper():
        return n2l(l2n(l) + s)
    else:
        return (n2l(l2n(l) + s)).lower()


if __name__ == '__main__':
    print('A: ', n2l(0))
    print('N: ', n2l(13))
    print('23: ', l2n('X'))
    print('1: ', l2n('B'))
    print('A: ',l2n2ls('A'))
    print('a: ',l2n2ls('a'))
