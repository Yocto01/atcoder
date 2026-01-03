N = int(input())
res = {}
n = int(N ** 0.5)
for y in range(2,n+1):
    for x in range(1,y):
        val = x*x + y*y
        if val > N:
            break
        if val in res:
            if res[val]:
                res[val] = False
        else:
            res[val] = True
res2 = []
for k,v in res.items():
    if v:
        res2.append(k)
#res2 = filter(lambda x : x[1] == 1, res.items())
res2 = sorted(res2)
res2 = list(map(lambda x : str(x), res2))
print(len(res2))
str = " ".join(res2)
if len(res2) != 0:
    print(str)

