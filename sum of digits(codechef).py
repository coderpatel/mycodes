n = int(input())

def digitsum(x):
    b = [int(i) for i in str(x)]
    res = sum(b)
    return res

list1 = []

for i in range(0,n):

    a = str(input())

    list1.append(a)

for i in range(0,n):
    

    print(digitsum(list1[i]))

    
