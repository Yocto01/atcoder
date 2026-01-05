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

import math

def calcpos(l,t,e):
    x = 0
    y = (l/2)*math.cos(2*math.pi/t*(-e)-math.pi/2)
    z = (l/2)*math.sin(2*math.pi/t*(-e)-math.pi/2) + l/2
    return x,y,z
def calcarg(ex,ey,ez,tx,ty,tz):
    ax = tx-ex 
    ay = ty-ey 
    az = 0 
    bx = ax 
    by = ay 
    bz = tz-ez 
    cos = (ax*bx+ay*by+az*bz)/(math.sqrt(ax**2+ay**2+az**2)*math.sqrt(bx**2+by**2+bz**2))
    if cos >= 1:
        cos = 1
    elif cos <= -1:
        cos = -1
    return math.acos(cos)

T = inputN()
L,X,Y = inputMN()

Q = inputN()
for i in range(Q):
    e = inputN()
    ex,ey,ez = calcpos(L,T,e)
    arg = calcarg(ex,ey,ez,X,Y,0)
    arg *= 180/math.pi
    print(arg)