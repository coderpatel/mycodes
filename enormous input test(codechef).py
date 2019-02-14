n,k = input().split()

n = int(n)
k = int(k)
c= 0

for i in range(0,n):
    ti = int(input())
    if ti%k == 0:
        c+=1

print(c)
