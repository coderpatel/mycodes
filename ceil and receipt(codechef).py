n = int(input())
list1=[]
for i in range(n):
    list1.append(int(input()))
menu=0
for i in range(n):
    while list1[i]!=0:
        if list1[i]>2048:
            list1[i]-=2048
            menu+=1
        else:
            a = list1[i]%2
            if a==1:
                menu+=1
            list1[i]//=2
    print(menu)
    menu=0
        
        
            

        

    
