def isPalindrome(x):
    
    if x<0: return False
    if x==0: return False

    x1 = 0
    x2 = x
    while(x>0):
        x1 *= 10
        x1 += x%10
        x //= 10 
            
    if x1 == x2:
        return True
    else:  return False


x=121
print(isPalindrome(x))