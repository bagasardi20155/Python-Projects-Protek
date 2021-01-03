from datetime import *
import os

if(os.path.exists("dataPinjaman.txt")) :
    fileMode = 'a'

else :
    fileMode = 'w'

file = open("dataPinjaman.txt", fileMode)

while True :
    

    kode_member = input("Masukkan Kode Member : ")
    nama_member = input("Masukkan Nama Member : ")
    judul_buku = input("Masukkan Judul Buku : ")

    tgl_pinjam = date.today()
    tgl_kembali = tgl_pinjam + timedelta(days = 7)

    dataPinjaman = [kode_member, nama_member, judul_buku, str(tgl_pinjam), str(tgl_kembali) + '\n']
    file.write('|'.join(dataPinjaman))

    ulangi = input("\nUlangi lagi (y/n) : ")

    if(ulangi.lower() == 'y') :
        continue

    elif(ulangi.lower() == 'n') :
        break

    else :
        print("Inputan tidak valid")
        break

file.close()
