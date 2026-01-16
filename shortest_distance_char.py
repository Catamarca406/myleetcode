def shortestToChar(s, c):
    last_c=0
    for i in range(len(s)):
        if s[i] == c:
            last_c = i
            break

    l = []    
    min_gap = 0
    i = 0

    for i in range(len(s)):
        if s[i] == c:
            last_c = i

        min_gap = abs(i - last_c)
        l.append(min_gap)

    for i in range(len(s)-1,-1,-1):
        if s[i] == c:
            last_c = i
        
        min_gap = abs(i - last_c)
        if l[i] > min_gap:
            l[i] = min_gap
            



    return l

s = "loveleetcode" 
c = 'e'
print(shortestToChar(s,c))