t = int(input())

list1 = []
for i in range(0,t):
    (a,b) = map(int,input().split())

    list1.append((a,b))

for i in range(t):

    print(list1[i][0]%list1[i][1])
