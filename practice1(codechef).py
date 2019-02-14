n = int(input())
list1=[]
for i in range(n):
    a = input()
    list1.append(a.lower())
    
for i in range(n):
    if ' not ' in list1[i]:
        print('Real Fancy')
    else:
        print('regularly fancy')
