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

N,K,X = inputMN()
S = inputG(N)
f = []
for a in itertools.product(list(range(N)),repeat=K):
    s = ''
    for b in a:
        s += S[b]
    f.append(s)
f = sorted(f)
print(f[X-1])
    