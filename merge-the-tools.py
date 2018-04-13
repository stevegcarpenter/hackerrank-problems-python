#!/usr/bin/env python3

# https://www.hackerrank.com/challenges/merge-the-tools/problem

def merge_the_tools(string, k):
    s = set()
    for i in range(len(string)):
        if string[i] not in s:
            print(string[i], end='')
            s.add(string[i])
        if (i + 1) % k == 0:
            print('')
            s = set()

