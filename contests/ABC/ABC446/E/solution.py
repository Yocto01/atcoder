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

M,A,B = inputMN()
lst = []
for i in range(10):
    lst.append(lst[-1]*A+lst[-2]*B)
print(lst)
cnt = 0
for i in range(M):
    for j in range(M):
        print("\(^o^)/")