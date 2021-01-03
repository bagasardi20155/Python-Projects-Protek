'''file = open('dataMhs.txt', 'r')

baris = file.readlines()

dicti = {}

for i in range(len(baris)) :
    a = baris[i].split('|')
    a[2] = a[2].replace('\n', '')
    
    dicti[i] = {'nama' : a[0], 'nim' : a[1], 'alamat' : a[2]}

print(dicti)

    

file = open('dataMhs.txt', 'r')

isiFile = file.readlines()
dataMhs = {}

for i in range(len(isiFile)) :

        replaced = isiFile[i].replace('\n', '')
        splitted = replaced.split('|')
        isiFile[i] = splitted

        dataMhs[i] = {'nim': isiFile[i][0], 'nama': isiFile[i][1], 'alamat': isiFile[i][2]}

    

print(dataMhs)'''



########################################################################
'''
file = open('dataMhs.txt', 'r')

nim = input('Masukkan NIM yang mau dicari : ')

isiFile = file.readlines()

status = 'ada'

for i in range(len(isiFile)) :
    if(nim in isiFile[i]) :

        status = 'ada'
        replaced = isiFile[i].replace('\n', '')
        splitted = replaced.split('|')
        
        break

    else :
        status = 'tidak ada'
        continue


if(status == 'ada') :
    
    print('Data Mahasiswa : ')
    print('NIM : ', splitted[0])
    print('Nama : ', splitted[1])
    print('Alamat : ', splitted[2])


else :
    print('Data mahasiswa tidak ditemukan')

'''
######################################################################
'''
file = open('angkaDijumlah.txt', 'r')

isiFile = file.readlines()

for i in range(len(isiFile)) :
    replaced = isiFile[i].replace('\n', '')
    splitted = replaced.split('|')
    
    hasil = int(splitted[0]) + int(splitted[1])

    isiFile[i] = hasil

print(isiFile)

file.close()

file2 = open('xxx.txt', 'w')

for x in range(len(isiFile)) :
    
    file2.write(str(isiFile[x]) + '\n')

file2.close()
'''
######################################################################
'''
def encrypt(teks, n) :
    listTeks = list(teks)

    result = []

    for i in range(len(listTeks)) :
        if(listTeks[i] != ' ') :
            a = ord(listTeks[i])
            b = a + n
            
            if(b > 90) :
                b = b - 26
                hasil = chr(b)
                result.append(hasil)
                
            else :
                hasil = chr(b)
                result.append(hasil)     

        else :
            result.append(listTeks[i])


    joined = ''.join(result)
    print(joined)


try :
    teks = input("Masukkan teks yang mau dirubah : ")
    n = int(input("Berapa jumlah geseran untuk setiap hurufnya ? "))

    encrypt(teks, n)
    

except ValueError :
    print("Inputan harus angka")

    '''
##############################################################

def decrypt(teks, n) :
    listTeks = list(teks)

    result = []

    for i in range(len(listTeks)) :
        if(listTeks[i] != ' ') :
            a = ord(listTeks[i])
            b = a - n
            
            if(b < 65) :
                b = b + 26
                hasil = chr(b)
                result.append(hasil)
                
            else :
                hasil = chr(b)
                result.append(hasil)     

        else :
            result.append(listTeks[i])


    joined = ''.join(result)
    print(joined)


try :
    teks = input("Masukkan teks yang mau dirubah : ")
    n = int(input("Berapa jumlah geseran untuk setiap hurufnya ? "))

    decrypt(teks, n)
    

except ValueError :
    print("Inputan harus angka")











































