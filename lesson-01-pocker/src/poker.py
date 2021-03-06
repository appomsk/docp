#!/usr/bin/python3

def straight(ranks):
    "Return True if the ordered ranks form a 5-card straight."
    start = ranks[0]
    stop  = ranks[0]-5
    step  = -1
    return tuple(range(start, stop, step)) == tuple(ranks)
    
def flush(hand):
    "Return True if all the cards have the same suit."
    ss = set((s for r, s in hand))
    return len(ss) == 1

def kind(n, ranks):
    """Return the first rank that this hand has exactly n of.
    Return None if there is no n-of-a-kind in the hand."""
    for r in ranks:
        if ranks.count(r) == n: return r
    
def two_pair(ranks):
    """If there are two pair, return the two ranks as a
    tuple: (highest, lowest); otherwise return None."""
    
    rst = set()
    for c in ranks:
        if ranks.count(c) == 2:
            rst.add(c)
    if len(rst) == 2:
        return (max(rst), min(rst))

def card_ranks(cards):
    "Return a list of the ranks, sorted with higher first."

    values = '--23456789TJQKA'
    ranks = [values.index(r) for r,s in cards]
    ranks.sort(reverse=True)

    if ranks == [14, 5, 4, 3, 2]:
        ranks = [5, 4, 3, 2, 1]

    return ranks

def hand_rank(hand):
# User Instructions
# 
# Modify the hand_rank function so that it returns the
# correct output for the remaining hand types, which are:
# full house, flush, straight, three of a kind, two pair,
# pair, and high card hands. 
# 
# Do this by completing each return statement below.
#
# You may assume the following behavior of each function:
#
# straight(ranks): returns True if the hand is a straight.
# flush(hand):     returns True if the hand is a flush.
# kind(n, ranks):  returns the first rank that the hand has
#                  exactly n of. For A hand with 4 sevens 
#                  this function would return 7.
# two_pair(ranks): if there is a two pair, this function 
#                  returns their corresponding ranks as a 
#                  tuple. For example, a hand with 2 twos
#                  and 2 fours would cause this function
#                  to return (4, 2).
# card_ranks(hand) returns an ORDERED tuple of the ranks 
#                  in a hand (where the order goes from
#                  highest to lowest rank). 
#
# Since we are assuming that some functions are already
# written, this code will not RUN. Clicking SUBMIT will 
# tell you if you are correct.
    ranks = card_ranks(hand)
    if straight(ranks) and flush(hand):            # straight flush
        return (8, max(ranks))
    elif kind(4, ranks):                           # 4 of a kind
        return (7, kind(4, ranks), kind(1, ranks))
    elif kind(3, ranks) and kind(2, ranks):        # full house
        return (6, kind(3, ranks), kind(2, ranks))
    elif flush(hand):                              # flush
        return (5, ranks) 
    elif straight(ranks):                          # straight
        return (4, max(ranks))
    elif kind(3, ranks):                           # 3 of a kind
        return (3, kind(3, ranks), ranks)
    elif two_pair(ranks):                          # 2 pair
        return (2, two_pair(ranks), ranks)
    elif kind(2, ranks):                           # kind
        return (1, kind(2, ranks), ranks )
    else:                                          # high card
        return (0, ranks)

    return max(hands, key=hand_rank)

def poker(hands):
    "Return a list of winning hands: poker([hand,...]) => [hand,...]"
    return allmax(hands, key=hand_rank)

def allmax(iterable, key=None):
    "Return a list of all items equal to the max of the iterable."

    key = key or (lambda x: x)

    if iterable:
        m = max(iterable, key=key)
        return [it for it in iterable if key(it) == key(m)]
    else:
        return iterable

if __name__ == '__main__':
    pass
