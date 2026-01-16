def addStrings(num1,num2):
    
    len1 = len(num1)
    len2 = len(num2)

    max_len=0

    if len1 > len2:
        max_len = len1
    else:
        max_len = len2

    i = len1-1
    j = len2 -1
    k = 0

    sum_elem,n1,n2,carry=0,0,0,0
    l=[]

    while i>=0 or j>=0 or carry:
        if i>=0:
            n1 = int(num1[i]) 
        else:
            n1 = 0
        if j>=0:
            n2 = int(num2[j])
        else:
            n2 = 0

        sum_elem = n1 + n2 + carry
        carry = sum_elem //10
        l.append(str(sum_elem % 10))

        if i >= 0:
            i-=1
        if j >= 0:
            j-=1
        k+=1

    s = "".join(l[::-1])
        

    return s        
    

num1="11"
num2="123"
print(addStrings(num1,num2))