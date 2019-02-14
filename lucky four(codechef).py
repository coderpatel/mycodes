n = int(input())
list2 = []
for i in range(n):
    a = input()
    list1 = [int(j) for j in str(a)]
    list2.append(list1)

for i in range(n):
    b = 0
    for j in range(len(list2[i])):
        c = int(list2[i][j])
        if c == 4:
            b += 1

    print(b)
        
