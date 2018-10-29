from util import n2l, l2n
from random import randint

def alphabet(shift):
    r = []
    e = lambda a: chr((a%26)+65)
    for l in range(0,25):
        r.append(e(l+shift))
    return r


if __name__ == '__main__':
    print(alphabet(0))
    print(alphabet(randint(0,25)))
