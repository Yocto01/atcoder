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
A = inputNA()
B = inputNA()
C = inputNA()

a46 = [0]*46
b46 = [0]*46
c46 = [0]*46

for i in range(N):
    a46[A[i]%46] += 1
    b46[B[i]%46] += 1
    c46[C[i]%46] += 1

res = 0
for a in range(46):
    for b in range(46):
        for c in range(46):
            if (a+b+c)%46 == 0:
                res += a46[a] * b46[b] * c46[c]
print(res)    