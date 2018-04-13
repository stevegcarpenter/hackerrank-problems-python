#!/usr/bin/env python3

# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

N = int(input())
print(sorted({int(x) for x in input().split()})[-2])
