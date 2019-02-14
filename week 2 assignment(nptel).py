def rotatelist(l,n):
    while n>0:
        l = l[1:]+l[0:1]
        n-=1
    return(l)
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

def chkprimes(n):
  c = 0
  if n%2 != 0:
    for i in range(1,n+1):
      if n%i == 0:
        c+=1
    if c == 2:
        return(True)

def primes(n):
  l = [2]
  for i in range(1,(n-1)):
    a=chkprimes(i)
    if a == True:
      l.append(i)
  return(l)

def primepartition(a):
  n = primes(a)
  j = 1
  first = n[0]
  last = n[len(n)-j]
  for i in range(len(n)):
    if first+last == a:
      return(True)
    if first + last > a:
      j-=1
    if first + last <a:
      first = n[i]
  return(False)
    
      
