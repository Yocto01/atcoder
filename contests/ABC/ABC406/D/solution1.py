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

xg = {}
yg = {}
xcounted = set()
ycounted = set()

for i in range(1,H+1):
    xg[i] = set()
for i in range(1,W+1):
    yg[i] = set()

for x,y in XY:
    xg[x].add(y)
    yg[y].add(x)
#print(xn)
#print(yn)

for q in query:
    if q[0] == 1:
        if q[1] in xcounted:
            print(0)
        else:
            print(len(xg[q[1]]-ycounted))
            xcounted.add(q[1])
        
    else:
        if q[1] in ycounted:
            print(0)
        else:
            print(len(yg[q[1]]-xcounted))
            ycounted.add(q[1])
    #print(xn)
    #print(yn)
