N = int(input())
A = list(map(int, input().split()))

dict = {}
for i,v in enumerate(A):
    if not v in dict:
        dict[v] = 1
    else:
        dict[v] += 1

res = 0
for v in dict.values():
    if v >= 2:
        res += (v * (v - 1) // 2) * (N - v)
        

print(res)