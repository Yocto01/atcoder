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
A = inputNA()
B = [0] * (N+1)

for i in range(N):
    B[i+1] += B[i] + A[i]
#print(A)

for i in range(Q):
    q = inputNA()
    #print(B)
    if q[0] == 1:
        B[q[1]] = B[q[1]-1] + A[q[1]]
        A[q[1]-1],A[q[1]] = A[q[1]],A[q[1]-1]
    else:
        print(B[q[2]] - B[q[1]-1])