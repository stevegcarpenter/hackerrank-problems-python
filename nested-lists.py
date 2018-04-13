#!/usr/bin/env python3

# https://www.hackerrank.com/challenges/nested-list/problem

n = int(input())
students = [[input(), float(input())] for _ in range(n)]
nextlowest = sorted(list(set([score for name, score in students])))[1]
print('\n'.join([name for name, score in sorted(students) if score == nextlowest]))

