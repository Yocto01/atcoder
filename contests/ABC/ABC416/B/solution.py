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

S = input()
T = ''
able = True
for c in S:
    if c == '.':
        if able:
            T += 'o'
            able = False            
        else:
            T += '.'
    if c == '#':
        able = True
        T += '#'
print(T)