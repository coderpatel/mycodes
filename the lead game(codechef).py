t = int(input())

a,b = 0,0
list1,list2 = [],[]

for i in range(0,t):

    c,d = map(int,input().split())

    a += c
    b += d

    list1.append(a)
    list2.append(b)

l,w,win = 0,0,0

for i in range(t):

    w = abs(list1[i]-list2[i])

    if w>l:
        l = w

        if list1[i]>list2[i]:
            win = 1

        else :
            win = 2
    
print(win,l)

    
