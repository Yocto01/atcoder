import bisect
import collections
import functools
import heapq
import queue
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

T = inputN()
for _ in range(T):
    n,d = inputMN()
    a = inputNA()
    b = inputNA()
    egg = [0]*(n*10+10)
    head = 0
    tail = 0
    
    for i in range(1,n+1):
        for j in range(a[i-1]):
            egg[tail] = i
            tail += 1
        for j in range(b[i-1]):
            egg[head] = 0
            head += 1
        if i - egg[head] == d and egg[head] != 0:
            tmp = egg[head]
            while tmp == egg[head]:
                egg[head] = 0
                head += 1
    print(tail-head)
    