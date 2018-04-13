#!/usr/bin/env python3

# https://www.hackerrank.com/challenges/finding-the-percentage/problem

n = int(input())
gradebook = {line[0]: list(map(float, line[1:])) for line in [input().split() for _ in range(n)]}
print('{:.2f}'.format(sum(gradebook[input()])/3))

