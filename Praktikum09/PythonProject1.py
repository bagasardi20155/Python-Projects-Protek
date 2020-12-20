def ubahHurufReplace(teks, a, b) :

    teksReplaced = teks.replace(a, b)
    return teksReplaced

def ubahHurufManual(teks, a, b) :

    listTeks = list(teks)
    for i in range(len(listTeks)) :
        
        if(listTeks[i] == a) :
            listTeks[i] = b
            
    teksReplaced = ''.join(listTeks)
    return teksReplaced

teks = input("Masukkan kata / kalimat yang anda ingin ubah : ")
a = input("Huruf / kata apa yang ingin anda rubah ? ")
b = input("Ubah {0} menjadi : ".format(a))

result = ubahHurufReplace(teks, a, b)
print(result)

hasil = ubahHurufManual(teks, a, b)
print(hasil)
