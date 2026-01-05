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
A = inputNA()
B = inputNA()

dif = 0
for i in range(N):
    dif += abs(A[i]-B[i])

if dif > K:
    print("No")
else:
    if (K - dif) % 2 == 0:
        print("Yes")
    else:
        print("No")
        