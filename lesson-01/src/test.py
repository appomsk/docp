#!/usr/bin/python3

from poker import *

def test():
    "Test cases for the functions in poker program"
    sf = "6C 7C 8C 9C TC".split() # Straight Flush
    fk = "9D 9H 9S 9C 7D".split() # Four of kind
    fh = "TD TC TH 7C 7D".split() # Full house
    tp = "5S 5D 9H 9C 6S".split() # Two pairs
    sf1 = "6C 7C 8C 9C TC".split() # Straight Flush
    sf2 = "6D 7D 8D 9D TD".split() # Straight Flush

    fkranks = card_ranks(fk)
    tpranks = card_ranks(tp)

    assert kind(4, fkranks) == 9
    assert kind(3, fkranks) == None
    assert kind(2, fkranks) == None
    assert kind(1, fkranks) == 7

    assert two_pair(fkranks) == None
    assert two_pair(tpranks) == (9, 5)

# add 3 new assert statements here.
    assert hand_rank(sf) == (8, 10)
    assert hand_rank(fk) == (7, 9, 7)
    assert hand_rank(fh) == (6, 10, 7)

    # Modify the test() function to include three new test cases.
    # These should assert that card_ranks gives the appropriate
    # output for the given straight flush, four of a kind, and
    # full house.
    #
    # For example, calling card_ranks on sf should output  
    # [10, 9, 8, 7, 6]
    assert card_ranks(sf) == [10, 9, 8, 7, 6]
    assert card_ranks(fk) == [9, 9, 9, 9, 7]
    assert card_ranks(fh) == [10, 10, 10, 7, 7]
    
    assert straight([9, 8, 7, 6, 5]) == True
    assert straight([9, 8, 8, 6, 5]) == False
    assert flush(sf) == True
    assert flush(fk) == False
    
    # Add 2 new assert statements here. The first 
    # should check that when fk plays fh, fk 
    # is the winner. The second should confirm that
    # fh playing against fh returns fh.
    assert poker([fk, fh]) == [fk]
    assert poker([fh, fh]) == [fh, fh]
    assert poker([sf, fk, fh]) == [sf]

    assert poker([sf1, sf2, fk, fh]) == [sf1, sf2]

    # Add 2 new assert statements here. The first 
    # should assert that when poker is called with a
    # single hand, it returns that hand. The second 
    # should check for the case of 100 hands.
    assert poker([sf]) == [sf]
    assert poker([sf] + [fh]*99) == [sf]
    print('tests passed')

if __name__ == '__main__':
    test()

