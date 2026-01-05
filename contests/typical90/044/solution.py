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

N,Q = inputMN()
A = inputNA()
shift = 0
for i in range(Q):
    t,x,y = inputMN()
    if t == 1:
        A[(x-1-shift)%N],A[(y-1-shift)%N] = A[(y-1-shift)%N],A[(x-1-shift)%N]
    if t == 2:
        shift += 1
    if t == 3:
        print(A[(x-1-shift)%N])
