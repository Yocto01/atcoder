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

N,M = inputMN()
rel = [0] * (N+1)

for i in range(M):
    a,b = inputMN()
    rel[a] += 1
    rel[b] += 1

ans = []
for i in range(1,N+1):
    if N-rel[i]-1 < 3:
        ans.append(0)
    else:
        ans.append(math.comb(N-rel[i]-1,3))

print(" ".join(map(str,ans)))