'''
Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, 
and you may not use the same element twice

'''

def two_sum(l,target):
    
    l.sort()           #ordino la lista 

    i=0
    j=len(l)-1

    while(i!=j):              #fino a che i!=j cerco le due somme spostandomi verso il centro della lista
        if(l[i]+l[j]) == target:
            return (i,j)
        elif (l[i]+l[j]) < target:
            i+=1
        else:
            j-=1

    if i==j:
        return -1
    

l = [2,7,11,15]
target = 9

print(two_sum(l,target))


