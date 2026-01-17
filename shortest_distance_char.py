def shortestToChar(s, c):
    last_c=0
    for i in range(len(s)):         #cerco il primo carattere 
        if s[i] == c:
            last_c = i
            break

    l = []    
    min_gap = 0
    i = 0

    for i in range(len(s)):
        if s[i] == c:   
            last_c = i              #aggiorno la posizione del carattere

        min_gap = abs(i - last_c)       #formula per calcolare la distanza
        l.append(min_gap)               #inserisco la distanza nell'array

    for i in range(len(s)-1,-1,-1):         #partendo dalla fine dell'array, controllo nuovamente le posizioni 
        if s[i] == c:
            last_c = i
        
        min_gap = abs(i - last_c)  
        if l[i] > min_gap:                  #verifico se la distanza precedente è > di quella appena trovata
            l[i] = min_gap
            



    return l                #ritorno la lista, ogni elem corrisponde alla distanza di ogni carattere a partire dal carattere cercato

s = "loveleetcode" 
c = 'e'
print(shortestToChar(s,c))