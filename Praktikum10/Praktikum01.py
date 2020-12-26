
file = open('angka.txt','r')

angka = file.readlines()

genap = []
ganjil = []

for i in range(len(angka)) :
    if('\n' in angka[i] == True) :
        angka[i].replace('\n', '')

        if(int(angka[i])%2 == 0) :
            genap.append(angka[i])
        else :
            ganjil.append(angka[i])

    else :
        if(int(angka[i])%2 == 0) :
            genap.append(angka[i])
        else :
            ganjil.append(angka[i])

print("Banyaknya bilangan genap : {0}".format(len(genap)))
print("Banyaknya bilangan ganjil : {0}".format(len(ganjil)))
