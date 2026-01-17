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

N,M,L,S,T = inputMN()
graph = {}
for i in range(1,N+1):
    graph[i] = []
for i in range(M):
    u,v,c = inputMN()
    graph[u].append([v,c])

precost = {}
cost = {}
cost[1] = [0]
#print(cost)
for i in range(L):
    precost = cost
    cost = {}
    for x in precost.keys():
        move = precost[x]
        for v,c in graph[x]:
            if not v in cost:
                cost[v] = []
            adarr = list(map(lambda x:x+c, filter(lambda x:x+c <= T, move)))
            #adarr = filter(lambda x: x <= T, adarr)
            cost[v] += adarr
    for j in cost.keys():
        cost[v] = list(set(cost[v]))
res = []
for i in range(1,N+1):
    if (not i in cost) or (len(cost[i]) == 0):
        continue
    if max(cost[i]) >= S:
        res.append(i)
            
print(*res)
            
        
    