from datetime import *

def diffDate(x) :

    listTgl = x.split("-")
    dateList = []

    for i in listTgl :
        dateList.append(int(i))

    ystrdy = date(dateList[0], dateList[1], dateList[2])
    today = datetime.date(datetime.now())

    delta = ystrdy - today
    result = delta.days

    return result
'''
try :
    tgl = input("Masukkan tanggal yang diinginkan dengan format (yyyy-mm-dd) : ")

    hasil = diffDate(tgl)

    print("Selisih tanggal {0} dengan hari ini adalah {1} hari".format(tgl, hasil))

except ValueError :
    print("Masukkan tanggal yang valid")

'''
