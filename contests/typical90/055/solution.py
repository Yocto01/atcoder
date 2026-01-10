import math
import itertools

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
N,P,Q = inputMN()
A = inputNA()

cnt = 0
for a in itertools.combinations(range(N),5):
    if (A[a[0]]*A[a[1]]%P*A[a[2]]%P*A[a[3]]%P*A[a[4]]%P)%P == Q:
        cnt += 1
print(cnt)