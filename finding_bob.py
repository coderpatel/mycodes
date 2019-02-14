c = 0
s = input(("Enter a string in lower case:"))
for i in range(2,(len(s))):
    #print(s[i])
    if s[i]=='b' and s[i]+s[i-1]+s[i-2] == 'bob':
        c+=1

print(c)
