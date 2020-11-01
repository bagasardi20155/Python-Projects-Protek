def luasSegitiga(a,t) :
    luas = a * t / 2
    return luas

alas = 10
tinggi = 20
print('Luas segitiga dengan alas ', alas,
        ' dan tinggi ', tinggi,
        ' adalah ', luasSegitiga(alas,tinggi))

alas2 = 15
tinggi2 = 45
print('Luas segitiga dengan alas ', alas2,
        ' dan tinggi ', tinggi2,
        ' adalah ', luasSegitiga(alas2,tinggi2))

#--------------------------------------------------------

def luasSegitiga2(a,t) :
    luas = a * t / 2
    print('Luas segitiga dengan alas ', a,
            ' dan tinggi ', t,
            ' adalah ', luas)

alas = 10
tinggi = 20
luasSegitiga2(alas,tinggi)

a = 15
t= 45
luasSegitiga2(a,t)
