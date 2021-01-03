from datetime import *
import Praktikum01

file = open("dataPinjaman.txt", "r")

isiFile = file.readlines()
kode_member = input("Masukkan Kode Member : ")

for i in range(len(isiFile)) :
    if(kode_member in isiFile[i]) :

        splitted = isiFile[i].split('|')
        status = 'ada'
        break

    else :
        status = 'tidak ada'
        continue


if(status == 'ada') :
    
    print("\nData Peminjaman Buku")
    print("Kode Member : ", splitted[0])
    print("Nama Member : ", splitted[1])
    print("Judul Buku : ", splitted[2])
    print("Tanggal Mulai Peminjaman : ", splitted[3])
    print("Tanggal Pengembalian : ", splitted[4])

    terlambat = Praktikum01.diffDate(splitted[4])
    denda = 2000 * abs(terlambat)

    if(terlambat >= 0) :
        print("Terlambat : 0 hari")
        print("Denda : 0")
        
    else :
        print("Terlambat : ", abs(terlambat))
        print("Denda : ", denda)
    
    

else :
    print("Data Peminjaman Tidak Ditemukan")
