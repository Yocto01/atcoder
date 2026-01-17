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
S = input()
T = input()
Q = inputN()
w = inputG(Q)

for i in range(Q):
    taka = True
    aoki = True
    for c in w[i]:
        if not c in S:
            taka = False
        elif not c in T:
            aoki = False
    if taka and (not aoki):
        print("Takahashi")
    elif (not taka) and aoki:
        print("Aoki")
    else:
        print("Unknown")