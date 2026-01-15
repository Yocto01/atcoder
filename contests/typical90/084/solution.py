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

N = inputN()
S = input()
S += "$"
res = N*(N-1)//2
prev = ""
cnt = 1
for i in range(N+1):
    if prev == S[i]:
        cnt += 1
    else:
        res -= cnt*(cnt-1)//2
        prev = S[i]
        cnt = 1
print(res)
