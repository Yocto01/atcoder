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

H,W,N = inputMN()
XY = inputNG(N)
Q = inputN()
query = inputNG(Q)

a = [[] for i in range(H+1)]
b = [[] for i in range(W+1)]
ux = [False] * (H+1)
uy = [False] * (W+1)
used = [False] * N

for i in range(N):
    x,y = XY[i]
    a[x].append(i)
    b[y].append(i)
for q in query:
    if q[0] == 1:
        if ux[q[1]]:
            print(0)
        else:
            ans = 0
            for e in a[q[1]]:
                if not used[e]:
                    used[e] = True
                    ans += 1
            ux[q[1]] = True
            print(ans)
    else:
        if uy[q[1]]:
            print(0)
        else:
            ans = 0
            for e in b[q[1]]:
                if not used[e]:
                    used[e] = True
                    ans += 1
            uy[q[1]] = True
            print(ans)