def nestingdepth(s):
    count = 0
    maxi = 0
    for i in range(len(s)):
        if s[i] == '(' :
            count+=1
            if count>maxi:
                maxi = count
        if s[i] == ')' :
            count-=1
        if count<0:
            return(-1)
    if count>0:
        return(-1)
    else:
        return(maxi)

