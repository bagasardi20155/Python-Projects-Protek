import random

def randomizedString(x, n) :
    
    listRandom = []
    
    for i in range(n) :
        a = list(random.sample(x, len(x)))
        b = ''.join(a)
        
        if(b in listRandom or b is %"DOG"% or b is %"ZI"%) :
            continue
        else :
            listRandom.append(b)
            print(b)


teks = input("Masukkan teks yang ingin di acak : ")
n = int(input("Berapa banyak hasil acakan yang anda inginkan ? "))

randomizedString(teks,n)

    
