import bisect
import collections
import functools
import heapq
import itertools
import math
import sys

def inputNum():
    return int(input())
def inputMultiNum():
    return map(int, input().split())
def inputNumArray():
    return list(map(int, input().split()))
def inputNumGrid(n):
    a = []
    for _ in range(n):
        a.append(list(map(int,input().split())))
    return a
def inputGrid(n):
    a = []
    for _ in range(n):
        a.append(input())
    return a

inputN = inputNum 
inputMN = inputMultiNum
inputNA = inputNumArray
inputNG = inputNumGrid
inputG = inputGrid

N = inputMN()
A = inputNA()

d = {}
for a in A:
    if not a in d:
        d[a+1] = 1
    else:
        if not a+1 in d:
            d[a+1] = d[a]+1
        else:
            d[a+1] = max(d[a]+1,d[a+1])
            d[a] = 0
print(max(list(d.values())))