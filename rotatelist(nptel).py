def rotatelist(l,n):
    while n>0:
        l = l[1:]+l[0:1]
        n-=1
    return(l)
