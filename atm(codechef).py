x,y = input().split()

x = float(x)
y = float(y)

if((x+0.5)<y and (x%5==0)): 
    y = y-(x+0.5)
    print(y)

else:
    print(y)

