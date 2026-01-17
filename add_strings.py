def addStrings(num1,num2):
    
    #inizializzo le lunghezze

    len1 = len(num1)
    len2 = len(num2)

    max_len=0

    if len1 > len2:         #verifico quale sia la stringa più lunga
        max_len = len1
    else:
        max_len = len2

    i = len1-1              #partendo dalla fine, devo sottrarre un valore, range -> (0-len-1)
    j = len2 -1
    k = 0

    sum_elem,n1,n2,carry=0,0,0,0   #inizializzo, somme e riporto
    l=[]

    while i>=0 or j>=0 or carry:   #mentre sono nel range delle stringhe
        if i>=0:
            n1 = int(num1[i])     #se i è ancora nel range, n1 assume il valore della stringa in pos 1, castata in int
        else:
            n1 = 0               #altrimenti n1 viene settato a 0
        if j>=0:                 #stesso per n2
            n2 = int(num2[j])
        else:
            n2 = 0

        sum_elem = n1 + n2 + carry          #sommo n1,n2, tenendo conto del riporto
        carry = sum_elem //10               #calcolo il riporto con mod(10)
        l.append(str(sum_elem % 10))        #inserisco nella lista la somma castata

        if i >= 0:                          #decremento se i e j sono ancora positivi, per rimanere nel range
            i-=1
        if j >= 0:
            j-=1
        k+=1

    s = "".join(l[::-1])                    #inserisco i caratteri nella mia stringa con join
                                            #faccio attenzione ad inserire i caratteri partendo dalla fine della stringa
        
    return s        
    

num1="11"
num2="123"
print(addStrings(num1,num2))