#Program untuk Menghitung berapa kali pengisian bahan bakar dalam sebuah perjalanan
import math

jarakTotal = 795
print('Jarak yang akan ditempuh Pak Budi adalah sejauh 795 km' + '\n')

jarakPerLiter = 12
print('Untuk 1 liter bensin, mobil Pak Budi dapat menempuh jarak sejauh 12 km' + '\n')

kapasitasTanki = 50
print('Kapasitas tanki mobil Pak Budi adalah 50 liter')

bensinYangDiperlukan = jarakTotal / jarakPerLiter
pengisian = (bensinYangDiperlukan - 50) /kapasitasTanki

minimalPengisian = math.ceil(pengisian)

print('Pak Budi harus mengisi mobilnya minimal sebanyak ' + str(minimalPengisian) + ' kali')

'''
#Jika ingin dinamis

print('============= Jumlah Bahan Bakar Yang Diperlukan =============')

jarakTotal = int(input('Berapa Kilometer Jarak yang Ingin Ditempuh ? '))
jarakPerLiter = int(input('Berapa Jarak yang Dapat Ditempuh Mobil dengan 1 Liter Bensin ? '))
kapasitasTanki = int(input('Berapa Kapasitas Tanki Mobil ? '))

bensinYangDiperlukan = jarakTotal / jarakPerLiter
pengisian = (bensinYangDiperlukan - 50) /kapasitasTanki

minimalPengisian = math.ceil(pengisian)

print('Pak Budi harus mengisi mobilnya minimal sebanyak ' + str(minimalPengisian) + ' kali')
'''
