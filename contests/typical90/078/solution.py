import bisect
import collections
import functools
import heapq
import itertools
import math

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
AB = inputNG(M)
rel = {}
for a,b in AB:
    if not (a in rel):
        rel[a] = []
    if not (b in rel):
        rel[b] = []
    rel[a].append(b)
    rel[b].append(a)

res = 0
for k in rel.keys():
    v = sorted(rel[k])
    if (bisect.bisect_left(v,k) == 1):
        res += 1
print(res)