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

N,L = inputMN()
K = inputN()
A = inputNA()

def check(x):
    num = 0
    pre = 0
    
    for i in range(N):
        if A[i] - pre >= x:
            num += 1
            pre = A[i]
            
    if L - pre >= x:
        num += 1
        
    return (num >= K + 1)

left = -1
right = L+1
while right - left > 1:
    mid = (left + right) // 2
    if check(mid):
        left = mid
    else:
        right = mid
print(left)