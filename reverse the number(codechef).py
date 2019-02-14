n = int(input())
list2=[]
for i in range(n):
    a = input()
    list2.append(a)

for i in range(n):
    b = list2[i]
    c = '0'
    for j in range(len(b)):
        c += str(int(b)%10)
        b = int(int(b)/10)
    print(int(c))
