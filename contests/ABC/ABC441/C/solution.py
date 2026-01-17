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

N,K,X = inputMN()
A = inputNA()

A.sort()
#print(A)
val = 0
for i in range(K):
    val += A[i]
if val < X:
    print(-1)
    sys.exit()
    
res = N - K
val = 0
for i in range(K):
    if val >= X:
        break
    val += A[K-1-i]
    res += 1
print(res)
    