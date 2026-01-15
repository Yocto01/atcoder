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

N = inputN()
A = inputNA()

S = sum(A)
if S%10 != 0:
    print("No")
    sys.exit()
s = S // 10

l = 0
r = 0
val = 0
while True:
    if l == N:
        print("No")
        break
    if val == s:
        print("Yes")
        break
    elif val < s:
        val += A[r%N]
        r += 1
    else:
        val -= A[l%N]
        l += 1        
    

    