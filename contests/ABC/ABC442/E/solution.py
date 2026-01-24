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

N,Q = inputMN()
XY = inputNG(N)

math.dps = 100
arg = []
for i in range(N):
    x,y = XY[i][0],XY[i][1]
    arg.append(-math.atan2(y,x))
sarg = sorted(arg)

#print(arg)
#print(sarg)

for i in range(Q):
    a,b = inputMN()
    ai,bi = bisect.bisect_left(sarg,arg[a-1]),bisect.bisect_right(sarg,arg[b-1])
    if ai < bi:
        print(bi-ai)
    else:
        print(N-(ai-bi)) 