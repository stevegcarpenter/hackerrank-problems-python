#!/bin/python3

# https://www.hackerrank.com/challenges/minimum-distances/problem

import sys

n = int(input().strip())
A = [int(A_temp) for A_temp in input().strip().split(' ')]
d = {}
min = n + 1

for i, val in enumerate(A):
    j = d.get(val)
    if j is None:
        d[val] = i
    else:
        if min > i - j:
            min = i - j

    if min == 1:
        break;

if min == n + 1:
    print(-1)
else:
    print(min)
