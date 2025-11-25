
'''
Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, 
and you may not use the same element twice

Versione con un dizionario 

'''


def two_sum(l,target):
    d={}
    for i in range(len(l)):      #utilizzo un dizionario per ordinare gli elementi
        elem = l[i]
        d[elem] = i 

    for i in range(len(l)):
        elem = l[i]
        if((target - elem) in d) and (i != d[target-elem]):
            return (i, d[target - elem])





l = [2,7,11,15]
target = 9

print(two_sum(l,target))
