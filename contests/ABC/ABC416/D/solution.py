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

T = inputN()
for _ in range(T):
    n,m = inputMN()
    a = inputNA()
    b = inputNA()
    
    a.sort()
    a.reverse()
    b.sort()
    b2 = list(map(lambda x:m-x,b))
    #print(a)
    #print(b2)

    ai = 0
    idx = 0
    cnt = 0
    while True:
        if idx == n:
            break
        if a[ai] < b2[idx]:
            idx += 1
        else:
            cnt += 1
            ai += 1
            idx += 1 
    print(sum(a) + sum(b) - m * cnt)