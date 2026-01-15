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

L,R = inputMN()

def count(n):
    cnt = 0
    sum = n*(n+1)//2
    for i in range(len(str(n))):
        cnt += sum - (10**i-1)*(10**i)//2
    return cnt

print((count(R) - count(L-1)) % (10**9+7))