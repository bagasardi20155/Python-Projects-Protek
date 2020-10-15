#Progam untuk menghitung Waktu tempuh

jarak1 = 125
kecepatan1 = 62
jarak2 = 256
kecepatan2 = 70

waktu1 = jarak1/kecepatan1
waktu2 = jarak2/kecepatan2
#waktu istirahat = 45 menit = 0.75 jam
waktuIstirahat = 0.75

# hasil waktuTotal adalah 6.4232718894009215 jam dalam float
waktuTotal = waktu1 + waktu2 + waktuIstirahat

# kemudian dikonversi menjadi menit dengan dikali 60, hasilnya 385.3963133640553 menit
totalMenit = waktuTotal*60

# totalMenit kemudian di // 60 untuk menghasilkan jam yaitu 6 jam
totalSemua = int(totalMenit//60)

# totalMenit kemudian di % 60 untuk menghasilkna menit yaitu 25 menit
totalSemua1 = int(totalMenit%60)

# untuk menghitung total waktu berkendara, yaitu dengan menggabungkan 6 jam 25 menit dalam string sehingga menjadi 6.25
totalFix = str(totalSemua) + str('.') + str(totalSemua1)

# untuk menghitung waktu sampai yaitu dengan mengubah 6.25 yang tadinya string menjadi float, kemudian ditambah jam berangkat
waktuSampai = 6 + float(totalFix)

print(waktuSampai)
