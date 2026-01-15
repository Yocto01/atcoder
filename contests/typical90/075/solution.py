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

def nfact(n):
    res = 0
    while n % 2 == 0:
        res += 1
        n //= 2
    m = n
    for b in range(3,math.floor(m**0.5)+1,2):
        if n%b == 0:
            while n%b == 0:
                res += 1
                n //= b
    if n != 1:
        res += 1
    return res


a = nfact(N)
print((a-1).bit_length())

