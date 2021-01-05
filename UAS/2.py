file = open("dataKaryawan.dat", "r")

isiFile = file.readlines()
print(isiFile)
kd_karyawan = input("Masukkan Kode Karyawan : ")


for i in range(len(isiFile)) :
    if(kd_karyawan in isiFile[i]) :

        replaced = isiFile[i].replace('\n', '')
        splitted = replaced.split('|')

dataKaryawan = {kd_karyawan : [splitted[1], splitted[2], splitted[3], splitted[4], splitted[5]]}

if(dataKaryawan[kd_karyawan][2] == "A") :
    gapok = 4000000

elif(dataKaryawan[kd_karyawan][2] == "B") :
    gapok = 4500000

else :
    gapok = 5000000

print("\nKode Karyawan : ", kd_karyawan)
print("Nama Karyawan : ", dataKaryawan[kd_karyawan][0])
print("Alamat Karyawan : ", dataKaryawan[kd_karyawan][1])
print("Golongan Karyawan : ", dataKaryawan[kd_karyawan][2])
print("Gapok Karyawan : Rp ", gapok)
print("Tanggal Lahir Karyawan : {0} (Usia: {1})".format(dataKaryawan[kd_karyawan][3], dataKaryawan[kd_karyawan][4]))
