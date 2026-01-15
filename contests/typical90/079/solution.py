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

H,W = inputMN()
A = inputNG(H)
B = inputNG(H)

dif = [[0 for j in range(W)] for i in range(H)]
for i in range(H):
    for j in range(W):
        dif[i][j] = B[i][j] - A[i][j]
#print(dif)

res = 0
pos = [[0,0],[0,1],[1,0],[1,1]]
for i in range(H-1):
    for j in range(W-1):
        res += abs(dif[i][j])
        tmp = dif[i][j]
        for x,y in pos:
            dif[i+x][j+y] -= tmp
same = True
for i in range(H):
    for j in range(W):
        if dif[i][j]:
            same = False
            break
if same:
    print("Yes")
    print(res)
else:
    print("No")
    