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

N,Q = inputMN()
A = inputNA()
LRV = inputNG(Q)

val = 0
a = []
for i in range(N-1):
    a.append(A[i+1] - A[i])

def sum(a):
    res = 0
    for n in a:
        res += abs(n)
    return res

res = sum(a)
for l,r,v in LRV:
    if l > 1:
        tmp = a[l-2]
        a[l-2] += v
        res += abs(a[l-2]) - abs(tmp)
    if r < N:
        tmp = a[r-1]
        a[r-1] -= v
        res += abs(a[r-1]) - abs(tmp)
    #print(a)
    print(res)