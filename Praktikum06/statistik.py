def jumlah(*n) :

    i = 0
    for x in n :
        i = i + x
    print(i)


def average(*n) :
    i = 0
    j = 0

    for x in n :
        i = i + x
        j += 1

    avg = i / j
    print(avg)


def maksimum(*n) :
    terbesar = n[0]
    for i in (n) :
        if(i > terbesar) :
            terbesar = i
    print(terbesar)


def minimum(*n) :
    terkecil = n[0]
    for i in (n) :
        if(i < terkecil) :
            terkecil = i
    print(terkecil)
