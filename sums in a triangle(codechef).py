'''n = int(input())
for i in range(n):
    m = int(input())
    list1=[]
    for j in range(m):
        list1.append(list(map(int,input().split())))
    print(list1)'''
for _ in range(int(input())):
    n=int(input())
    l=[]
    ans=[]
    for i in range(n):
        l.append(list(map(int,input().split())))
        ans.append(l[i])
    for i in range(n-2,-1,-1):
        for j in range(i+1):
            ans[i][j]+=max(ans[i+1][j],ans[i+1][j+1])
   # print(ans)
    print(ans[0][0])
        
    
        
