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

T = inputN()
for _ in range(T):
    #print(f"_ = {_}")
    n,w = inputMN()
    c = inputNA()
    if n < w:
        print(0)
        continue
    val = 0
    for i in range(w):
        val += c[i]
    a = [0] * (w * 2)
    val2 = val
    
    d = 0
    for i in range(n):
        a[i%(w*2)] += val
        #print(a)
        if (i+w) > n:
            a[-d] += val2
        val -= c[i]
        if i+w < n:
            val += c[i+w]
        else:
            val2 -= c[w-1-d]
            d += 1
    print(min(a))
    
        
    
