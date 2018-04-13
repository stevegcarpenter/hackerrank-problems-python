#!/usr/bin/env python3

# https://www.hackerrank.com/challenges/no-idea/problem

v, a, b = [input().split() for _ in range(4)][1:]
a = set(a); b = set(b)

happy = len([v[i] for i in range(len(v)) if v[i] in a]) - len([v[i] for i in range(len(v)) if v[i] in b])
print(happy)

