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

N,L = inputMN()

a = [0] * (N+1)
a[0] = 1
for i in range(1,N+1):
    if i+L-1 <= N:
        a[i+L-1] += a[i-1]
    a[i] += a[i-1]
print(a[-1]%(10**9+7))