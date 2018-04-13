#!/usr/bin/env python3

# https://www.hackerrank.com/challenges/python-lists/problem

n = int(input())
l = []
for _ in range(n):
    s = input().split()
    cmd = s[0]
    args = s[1:]
    if cmd !='print':
        cmd += '(' + ','.join(args) + ')'
        eval('l.'+cmd)
    else:
        print(l)
