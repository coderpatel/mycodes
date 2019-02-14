s = input()
lword = ''
cword = ''
i = 0
while i<len(s):
    while ord(s[i])>=ord(s[i-1]):
        cword+=s[i]
        i+=1
    if len(cword)>len(lword):
        lword = cword

print(lword)
