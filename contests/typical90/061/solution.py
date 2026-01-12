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

Q = inputN()
TX = inputNG(Q)

a = [0] * (2 * (10**5) + 100)
right = 10**5 + 50
left = 10**5 + 49

for t,x in TX:
    if t == 1:
        a[right] = x
        right += 1
    elif t == 2:
        a[left] = x
        left -= 1
    else:
        print(a[right-x])
