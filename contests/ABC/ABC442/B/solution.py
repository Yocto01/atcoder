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

val = 0
sound = False

Q = inputN()

for i in range(Q):
    a = inputN()
    if a == 1:
        val += 1
    if a == 2:
        val = max(0,val-1)
    if a == 3:
        sound = not sound
    if val >= 3 and sound:
        print("Yes")
    else:
        print("No")