N,M = map(int, input().split())
A = list(map(int, input().split()))

s = sum(A)
isM = False
for i in range(N):
    if s - A[i] == M:
        isM = True

print("Yes" if isM else "No")