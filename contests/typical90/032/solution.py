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
A = inputNG(N)
M = inputN()
cant = {}
for i in range(M):
    x,y = inputMN()
    if not x in cant:
        cant[x] = []
    if not y in cant:
        cant[y] = []
    cant[x].append(y)
    cant[y].append(x)
#print(cant)

def dfs(n,cant):
    stack = [[n]]
    mn = 10 ** 10
    
    while len(stack) != 0:
        #print(stack)
        now = stack.pop()
            
        for i in range(1,N+1):
            if i in now: continue
            if (now[-1] in cant) and (i in cant[now[-1]]): continue
            if len(now) == N-1:
                val = 0
                for j in range(N-1):
                    val += A[now[j]-1][j]
                val += A[i-1][N-1]
                #print(val)
                mn = min(mn,val)
            else:
                stack.append(now + [i])
            
    return mn
    

mn = 10 ** 10
for i in range(1,N+1):
    val = dfs(i,cant)
    mn = min(mn,val)
    
print(mn if mn != 10 ** 10 else -1)