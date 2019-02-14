n = int(input())
list1=[]
for i in range(n):
    a,b = input().split()
    a = int(a)
    b = int(b)
    list1.append([a,b])
for i in range(n):
    mi = max(list1[i])
    ma = sum(list1[i])
    print(mi ,ma)


