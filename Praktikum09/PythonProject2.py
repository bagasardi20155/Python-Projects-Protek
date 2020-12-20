def bintang(n) :

    for i in range(n) :

        count = i + 1
        star = "*" * (i + count)
        print(star.center(10))


bintang(4)
