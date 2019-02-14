n = int(input())
list2 = []

for i in range(n):
    a = input()
    list1 = [int(j) for j in str(a)]

    list2.append(list1)

for i in range(n):
    print(list2[i][0]+list2[i][-1])
