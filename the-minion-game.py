#!/usr/bin/env python3

# https://www.hackerrank.com/challenges/the-minion-game/problem

def minion_game(string):
    vowels = {'A', 'E', 'I', 'O', 'U'}
    score_k, score_s, ln = (0, 0, len(s))

    for i in range(ln):
        if s[i] in vowels:
            score_k += (ln - i)
        else:
            score_s += (ln - i)

    if score_k > score_s:
        print('Kevin {}'.format(score_k))
    elif score_k < score_s:
        print('Stuart {}'.format(score_s))
    else:
        print('Draw')

