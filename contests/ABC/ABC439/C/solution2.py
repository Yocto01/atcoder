N = int(input())
res = [0] * (N+1)
n = int(N ** 0.5)
for y in range(2,n+1):
    for x in range(1,y):
        val = x*x + y*y
        if val > N:
            break
        res[val] += 1
res2 = []
for i in range(1,N+1):
    if res[i] == 1:
        res2.append(str(i))
print(len(res2))
str = " ".join(res2)
if len(res2) != 0:
    print(str)

