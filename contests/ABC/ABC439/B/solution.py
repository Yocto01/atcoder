def do(n):
    val = 0
    while n != 0:
        val += (n%10)**2
        n = n//10
    return val

def isHappy(n):
    log = []
    val = n
    while val != 1:
        val = do(val)
        if val in log:
            return "No"
        log.append(val)
    return "Yes"
    
N = int(input())
print(isHappy(N))