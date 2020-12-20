def bintang(n) :

    puncak = (n+1)/2
    x = 3
    
    for i in range(n) :
        
        if(i < puncak) :
            count = i + 1
        else :
            count = i - x
            x = x + 4
            
        star = "*" * (i + count)
        print(star.center(20))

        
bintang(7)
