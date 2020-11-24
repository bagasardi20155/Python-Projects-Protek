
try :

    # membukan dan mau membaca file F:\DOKUMEN KULIAH SMT 1\Pemrograman Terstruktur\Praktikum 7\data.txt
    file = open("F:\DOKUMEN KULIAH SMT 1\Pemrograman Terstruktur\Praktikum 7\data.txt", "r")

    # baca baris pertama dari file
    # simpan ke dalam variable bil1 sbg integer
    bil1 = int(file.readline())

    # baca baris kedue dari file
    # simpan ke dalam variable bil2 sbg integer
    bil2 = int(file.readline())

    # hitung dan tampilkan hasil bagi
    hasil = bil1/bil2
    print(bil1, 'dibagi', bil2, '=', hasil)

except FileNotFoundError :
    print('File tidak ditemukan')

except ZeroDivisionError :
    print('Tidak boleh pembagian dengan nol !')
    
