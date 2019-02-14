t = int(input())

for i in range(0,t):
    n = int(input())
    m = n
    for j in range(0,(n-1)):
        n -= 1
        m = m*n
    print(m)


