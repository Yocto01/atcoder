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
    mn = -1
    
    while len(stack) != 0:
        #print(stack)
        now = stack.pop()
        
        if len(now) == N:
            val = 0
            for i in range(N):
                val += A[now[i]-1][i]
            #print(val)
            if mn == -1 or mn > val:
                    mn = val
        for i in range(1,N+1):
            if i in now: continue
            if (now[-1] in cant) and (i in cant[now[-1]]): continue
            stack.append(now + [i])
            
    return mn
    

mn = -1
for i in range(1,N+1):
    val = dfs(i,cant)
    if val > 0:
        if mn == -1: mn = val
        mn = min(mn,val)
    
print(mn)