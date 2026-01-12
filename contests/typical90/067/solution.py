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

N,K = inputMN()
N = str(N)

def base10to9(n):
    res = ''
    if n == 0:
        return '0'
    while n != 0:
        res += str(n % 9)
        n //= 9
    
    return res[::-1]

for i in range(K):
    #print(int(N,8))
    N = base10to9(int(N,8))
    #print(N)
    N = N.replace('8','5')
    #print(N)
print(N)