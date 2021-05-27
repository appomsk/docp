#!/usr/bin/python3

import random

# This builds a deck of 52 cards. If you are unfamiliar
# with this notation, check out Andy's supplemental video
# on list comprehensions (you can find the link in the 
# Instructor Comments box below).

# does not work for numhands >10
def deal(numhands, n=5, deck=[r+s for r in '23456789TJQKA' for s in 'SHDC']):
    random.shuffle(deck)
    rst = []
    for i in range(numhands):
        rst.append(deck[i*n:(i+1)*n])
    return rst

if __name__ == '__main__':
    print(deal(5))

