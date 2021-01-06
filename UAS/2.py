def getGapok(gol) :
    if(gol == "A") :
        gapok = 4000000

    elif(gol == "B") :
        gapok = 4500000

    else :
        gapok = 5000000

    return gapok

file = open("dataKaryawan.dat", "r")

isiFile = file.readlines()
kd_karyawan = input("Masukkan Kode Karyawan : ")

dataKaryawan = {}
try :
    for i in range(len(isiFile)) :

            replaced = isiFile[i].replace('\n', '')
            splitted = replaced.split('|')
        
            dataKaryawan[splitted[0]] = [splitted[1], splitted[2], splitted[3], splitted[4], splitted[5]]

    print(dataKaryawan)
    gaji = getGapok(dataKaryawan[kd_karyawan][2])
    
    
    print("\nKode Karyawan : ", kd_karyawan)
    print("Nama Karyawan : ", dataKaryawan[kd_karyawan][0])
    print("Alamat Karyawan : ", dataKaryawan[kd_karyawan][1])
    print("Golongan Karyawan : ", dataKaryawan[kd_karyawan][2])
    print("Gapok Karyawan : Rp ", gaji)
    print("Tanggal Lahir Karyawan : {0} (Usia: {1})".format(dataKaryawan[kd_karyawan][3], dataKaryawan[kd_karyawan][4]))

except NameError :
    print("Data tidak Ditemukan")
