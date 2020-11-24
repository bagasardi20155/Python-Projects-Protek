#Program untuk menampilkan Struk Rincian Gaji Karyawan

kodeKaryawan = input('Masukkan kode karyawan   : ')
namaKaryawan = input('Masukkan nama karyawan  : ')
gol = input('Masukkan golongan            : ')

status = input('Masukkan Status (1: menikah, 2: belum) : ')

if(status == '1') :
    statusMenikah = 'Sudah Menikah'
    tunjanganMenikah = 10/100
    jmlAnak = int(input('Masukkan Jumlah Anak      : '))
    tunjanganAnak = 5/100 * jmlAnak
else :
    jmlAnak = 0
    statusMenikah = 'Belum Menikah'
    tunjanganMenikah = 0
    tunjanganAnak = 0
    

print('+ ================================= +' + '\n')
print('       STRUK RINCIAN GAJI KARYAWAN' + '\n')
print('+ --------------------------------- +' + '\n')

print('Nama Karyawan     : '  + namaKaryawan + ' (Kode: '+ kodeKaryawan + ')')
print('Golongan               : ' + gol + '\n')
print('Status Menikah       : ' + statusMenikah)
print('Jumlah Anak          : ' + str(jmlAnak))
print('+ --------------------------------- +' + '\n')

if(gol == 'A') :
    gajiPokok = 10000000
    potongan = 2.5
    jmlTunjanganMenikah = 10000000 * tunjanganMenikah
    jmlTunjanganAnak = 10000000 * tunjanganAnak
    
    gajiSebelumDipotong = 10000000 + jmlTunjanganMenikah + jmlTunjanganAnak
    jumlahPotongan = gajiSebelumDipotong * potongan / 100
    gajiSetelahDipotong = gajiSebelumDipotong - jumlahPotongan
    

elif(gol == 'B') :
    gajiPokok = 8500000
    potongan = 2.0
    jmlTunjanganMenikah = 8500000 * tunjanganMenikah
    jmlTunjanganAnak = 8500000 * tunjanganAnak
    
    gajiSebelumDipotong = 8500000 + jmlTunjanganMenikah + jmlTunjanganAnak
    jumlahPotongan = gajiSebelumDipotong * potongan / 100
    gajiSetelahDipotong = gajiSebelumDipotong - jumlahPotongan


elif(gol == 'C') :
    gajiPokok = 7000000
    potongan = 1.5
    jmlTunjanganMenikah = 7000000 * tunjanganMenikah
    jmlTunjanganAnak = 7000000 * tunjanganAnak
    
    gajiSebelumDipotong = 7000000 + jmlTunjanganMenikah + jmlTunjanganAnak
    jumlahPotongan = gajiSebelumDipotong * potongan / 100
    gajiSetelahDipotong = gajiSebelumDipotong - jumlahPotongan


elif(gol == 'D') :
    gajiPokok = 5500000
    potongan = 1.0
    jmlTunjanganMenikah = 5500000 * tunjanganMenikah
    jmlTunjanganAnak = 5500000 * tunjanganAnak
    
    gajiSebelumDipotong = 5500000 + jmlTunjanganMenikah + jmlTunjanganAnak
    jumlahPotongan = gajiSebelumDipotong * potongan / 100
    gajiSetelahDipotong = gajiSebelumDipotong - jumlahPotongan


print('Gaji Pokok             : Rp ' + str(gajiPokok))
print('Tunjangan Menikah  : Rp ' + str(jmlTunjanganMenikah))
print('Tunjangan Anak      : Rp ' + str(jmlTunjanganAnak))
print('+ ------------------------------- - +' + '\n')

print('Gaji Kotor              : Rp ' + str(gajiSebelumDipotong))
print('Potongan ( ' + str(potongan) +' % )  : Rp ' + str(jumlahPotongan) + '\n')
print('+ ------------------------------- - +' + '\n')

print('Gaji Bersih           : Rp ' + str(gajiSetelahDipotong))
    
