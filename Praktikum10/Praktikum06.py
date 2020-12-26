def encrypt(teks, n) :
    
    listTeks = list(teks)

    for i in range(len(listTeks)) :
        if(listTeks[i] != ' ') :
            if(ord(listTeks[i]) + n < 90) :
                
                asciiCode = ord(listTeks[i])
                encrypted = asciiCode + n
                listTeks[i] = chr(encrypted)

            else :
                
                asciiCode = ord(listTeks[i])
                encrypted = (asciiCode + n) - 26
                listTeks[i] = chr(encrypted)

        else :
            
            continue

    result = ''.join(listTeks)

    return result


try :
    
    teks = input("Masukkan teks yang ingin di enkripsi : ")
    n = int(input("Berapa jumlah geseran enkripsi : "))

    hasil = encrypt(teks, n)
    print("\nHasil pengenkripsian dari teks {0} adalah : {1}".format(teks, hasil))

except ValueError :
    print("Masukkan hanya bilangan bulat")
