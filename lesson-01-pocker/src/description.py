#!/usr/bin/python3

def description():
    print( '''
Faces - King, Quien, Jack 

Suits - Hearts, Clubs, Diamonds, Spades
Unicode:
♠	2660	♡	2661	♢	2662	♣	2663

Royal flush
A, K, Q, J, 10, all the same suit.
Straight flush
Five cards in a sequence, all in the same suit.
Four of a kind
All four cards of the same rank.
Full house
Three of a kind with a pair.
Flush
Any five cards of the same suit, but not in a sequence.
Straight
Five cards in a sequence, but not of the same suit.
Three of a kind
Three cards of the same rank.
Two pair
Two different pairs.
Pair
Two cards of the same rank.
High Card''')


if __name__ == '__main__':
    description()

