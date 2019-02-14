def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    a = len(aStr)
    if a == 0:
        return False
    if a == 1 and char == aStr:
        return True
    if a%2 == 0:
        aStr = aStr[:]+aStr[(a-1)]
        upper = aStr[a]
    else:
        upper = aStr[(a-1)]
    mid = aStr[(a-1)//2]
    lower = aStr[0]
    if mid == upper and mid == lower:
        return False
    if char == mid:
        return True
    if char > mid:
        return isIn(char,aStr[aStr.index(mid):])
    if char < mid:
        return isIn(char,aStr[:aStr.index(mid)])
    
        
