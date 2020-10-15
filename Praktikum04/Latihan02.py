#Program Untuk Menghitung Jumlah Bahan Bakar yang diperlukan dalam sebuah perjalanan

jarakTotal = 795
print('Jarak yang akan ditempuh Pak Budi adalah sejauh 795 km' + '\n')

jarakPerLiter = 12
print('Untuk 1 liter bensin, mobil Pak Budi dapat menempuh jarak sejauh 12 km' + '\n')

bensinYangDiperlukan = jarakTotal / jarakPerLiter
print('Bensin Yang Diperlukan adalah ' + str(bensinYangDiperlukan))

#Jika ingin menggunakan data yang dinamis

'''

print('============= Jumlah Bahan Bakar Yang Diperlukan =============')

jarakTotal = int(input('Berapa Kilometer Jarak yang Ingin Ditempuh ? '))
jarakPerLiter = int(input('Berapa Jarak yang Dapat Ditempuh Mobil dengan 1 Liter Bensin ? '))

bensinYangDiperlukan = jarakTotal / jarakPerLiter

print('Bensin Yang Diperlukan adalah ' + str(bensinYangDiperlukan))

'''
