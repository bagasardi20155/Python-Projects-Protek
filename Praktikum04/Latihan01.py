#Program untuk Permasalahan Biaya Sewa Rental Mobil

#Variable assignment
jamAmbil  = 6
menitAmbil = 00
print('Mobil mulai disewa pada pukul 06.00')

jamBalik = 23
menitBalik = 50
print('Mobil dikembalikan pada pukul 23.50')

#Operasi Penghitungan Biaya Sewa
jamSewa = jamBalik - jamAmbil
menitSewa = menitBalik - menitAmbil

lamaSewa = jamSewa + menitSewa / 60

totalSewa = int(lamaSewa)

totalBiaya = 200000 + (10000*(totalSewa - 12))

#Tampilkan Hasil
print('Biaya yang perlu dibayarkan untuk rental mobil adalah : ' + str(totalBiaya))
        

# Jika ingin dinamis

'''
print('================== Rental Mobil ==================')

jamCheckIn,menitCheckIn = input('Mobil disewa pada pukul (hh:mm)  ').split(':')

jamCheckOut,menitCheckOut = input('Mobil dikembalikan pada pukul(hh:mm) ').split(':')

#Mengambil data yang diinputkan dan mengcastingnya menjadi integer
jamAmbil = int(jamCheckIn)
menitAmbil = int(menitCheckIn)
jamBalik = int(jamCheckOut)
menitBalik = int(menitCheckOut)

#Menghitung berapa jam mobil disewa, untuk selisih menit jika lebih dari 30 menit akan dihitung 1 jam
menitSewa = menitBalik - menitAmbil
if(menitSewa > 30) :
    jamSewa = (jamBalik - jamAmbil) + 1
elif(menitSewa <= 30) :
    jamSewa = (jamBalik - jamAmbil)
    
#Menampilkan hasil penghitungan penyewaan mobil
if(jamSewa == 12 or jamSewa < 12) :
        print('Biaya Sewa Mobil adalah Sebesar : Rp. 200,000')
elif(jamSewa > 12):
        biayaSewa = 200000 + (10000 * (jamSewa - 12))
        print('Biaya Sewa Mobil adalah Sebesar : Rp. ' + str(biayaSewa))
else :
        print('Masukkan jam mobil disewa dan dikembalikan yang valid !')
'''
