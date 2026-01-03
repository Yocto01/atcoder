N = int(input())
A = list(map(int, input().split()))
a = {}
b = {}
c = {}
for i in range(N):
    if A[i]%3 == 0:
        if A[i] in a:
            a[A[i]].append(i)
        else:
            a[A[i]] = [i]
    elif A[i]%5 == 0:
        if A[i] in a:
            b[A[i]].append(i)
        else:
            b[A[i]] = [i]
    elif A[i]%7 == 0:
        if A[i] in a:
            c[A[i]].append(i)
        else:
            c[A[i]] = [i]
for k,v in b.items():
    a2 = a[b//5*3]
    c2 = c[b//5*7]
    a_left = 0
    a_right = 0
    c_left = 0
    a_right = 0
    for i in a2:
        pass
        
    

print(a)
print(b)
print(c)

