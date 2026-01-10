import math
import heapq

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
AB = inputNG(N)
sub = []
heapq.heapify(sub)
AB = sorted(AB,key=lambda x: x[1],reverse=True)
AB.append([0,0])
res = 0
ptr = 0
m_sub = 0
for i in range(K):
    if len(sub) != 0:
        m_sub = sub[0]*(-1)
    if m_sub > AB[ptr][1]:
        heapq.heappop(sub)
        res += m_sub
        #print(2,m_sub)
        m_sub = 0
    else:
        res += AB[ptr][1]
        #print(1,AB[ptr][1])
        heapq.heappush(sub,AB[ptr][1] - AB[ptr][0])
        if ptr < N: ptr += 1
        
    #print(res)
    #print(sub)
print(res)