import math
n = int(input())
list1=[]
for i in range(n):
    list1.append(int(input()))
for i in range(n):
    print(int(math.sqrt(list1[i])))
