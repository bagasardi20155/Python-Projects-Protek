def decrypt(teks, n) :
    
    listTeks = list(teks)

    for i in range(len(listTeks)) :
        if(listTeks[i] != ' ') :
            if(ord(listTeks[i]) - n >= 65) :
                
                asciiCode = ord(listTeks[i])
                decrypted = asciiCode - n
                listTeks[i] = chr(decrypted)

            else :
                
                asciiCode = ord(listTeks[i])
                decrypted = (asciiCode + 26) - n
                listTeks[i] = chr(decrypted)

        else :
            
            continue

    result = ''.join(listTeks)

    return result


try :
    
    teks = input("Masukkan teks yang ingin di enkripsi : ")
    n = int(input("Berapa jumlah geseran enkripsi : "))

    hasil = decrypt(teks, n)
    print("\nHasil pengenkripsian dari teks {0} adalah : {1}".format(teks, hasil))

except ValueError :
    print("Masukkan hanya bilangan bulat")
