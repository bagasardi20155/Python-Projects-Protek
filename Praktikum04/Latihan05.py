#Program untuk membuat 'diagram'  jumlah siswa

print('============== Program Membuat Diagram Jumlah Siswa =============='+'\n')

lakiLaki = int(input('Berapa jumlah mahasiswa laki - laki di jurusan PTIK UNS ? '))
perempuan = int(input('Berapa jumlah mahasiswa perempuan di jurusan PTIK UNS ? '))

lk = int(lakiLaki/10)
pr = int(perempuan/10)
print('======================'+'\n')

print('Laki - laki = ' + '*' * lk)
print('Perempuan = ' + '*' * pr)


