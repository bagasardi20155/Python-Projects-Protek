import os
from datetime import *


if(os.path.exists) :
        fileMode = 'a'

else :
        fileMode = 'w'

file = open("dataKaryawan.dat", fileMode)


    
def addKaryawan(nip, nama, alamat, gol, tgl_lahir, usia) :

    listData = [nip, nama, alamat, gol, tgl_lahir, str(usia) + '\n']
    file.write('|'.join(listData))



def getUsia(tgl_lahir) :
    
    listTgl = tgl_lahir.split('-')

    thn_lahir = int(listTgl[0])
    thn_skrg = datetime.now()

    usia = thn_skrg.year - thn_lahir

    return usia


while True :
    
    nip = input("\nMasukkan NIP : ")
    nama = input("Masukkan Nama : ")
    alamat = input("Masukkan Alamat : ")
    gol = input("Masukkan Golongan (A / B / C) : ")

    
    if(gol.lower() == 'a' or gol.lower() == 'b' or gol.lower() == 'c') :

        tgl_lahir = input("Masukkan Tgl Lahir (Format : yyyy-mm-dd) :")
        umur = getUsia(tgl_lahir)

        try :
            if(datetime.strptime(tgl_lahir, '%Y-%m-%d')) :

                tambah = input("\nTambah data (y / n) : ")

                if(tambah.lower() == 'y') :
                    addKaryawan(nip,nama,alamat,gol,tgl_lahir,umur)
                    continue
            
                elif(tambah.lower() == 'n') :
                    addKaryawan(nip,nama,alamat,gol,tgl_lahir,umur)
                    break
            
                else :
                    print("Inputan Tidak Valid")
                    addKaryawan(nip,nama,alamat,gol,tgl_lahir,umur)
                    break
            
        except ValueError :
            print("Inputan Tidak Valid")
            continue
    
    else :
        print("Inputan Tidak Valid")
        continue


file.close()
