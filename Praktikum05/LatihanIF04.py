#Program untuk menampilkan Struk Rincian Gaji Karyawan

kodeKaryawan = input('Masukkan kode karyawan   : ')
namaKaryawan = input('Masukkan nama karyawan  : ')
gol = input('Masukkan golongan            : ')
print('')
gajiPokok = 0
potongan = 0

print('+ ================================= +' + '\n')
print('       STRUK RINCIAN GAJI KARYAWAN' + '\n')
print('+ --------------------------------- +' + '\n')

print('Nama Karyawan     : '  + namaKaryawan + ' (Kode: '+ kodeKaryawan + ')')
print('Golongan               : ' + gol + '\n')
print('+ --------------------------------- +' + '\n')

if(gol == 'A') :
    gajiPokok = 10000000
    potongan = 2.5
    jumlahPotongan = 10000000 * potongan / 100
    gajiSetelahDipotong = 10000000 - jumlahPotongan
    

elif(gol == 'B') :
    gajiPokok = 8500000
    potongan = 2.0
    jumlahPotongan = 8500000 * potongan / 100
    gajiSetelahDipotong = 8500000 - jumlahPotongan


elif(gol == 'C') :
    gajiPokok = 7000000
    potongan = 1.5
    jumlahPotongan = 7000000 * potongan / 100
    gajiSetelahDipotong = 7000000 - jumlahPotongan


elif(gol == 'D') :
    gajiPokok = 5500000
    potongan = 1.0
    jumlahPotongan = 5500000 * potongan / 100
    gajiSetelahDipotong = 5500000 - jumlahPotongan


print('Gaji Pokok             : Rp ' + str(gajiPokok))
print('Potongan ( ' + str(potongan) +' % )  : Rp ' + str(jumlahPotongan) + '\n')
print('+ ------------------------------- - +' + '\n')
print('Gaji Bersih           : Rp ' + str(gajiSetelahDipotong))
    
