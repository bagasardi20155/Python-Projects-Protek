mhs = ['K001:ROSIHAN ARI:1979-09-01:SOLO',
       'K002:DWI AMALIA FITRIANI:1979-09-17:KUDUS',
       'K003:FAZA FAUZAN:2005-01-28:KARANGANYAR']

listBaru = []

for i in range(len(mhs)) :
    a = mhs[i].split(':')
    listBaru.append(a)

    b = listBaru[i][2].split('-')
    b.reverse()
    
    bJoined = '/'.join(b)
    listBaru[i][2] = bJoined


print('=' * 65)
print('NIM'.ljust(10), 'NAMA MAHASISWA'.ljust(20), 'TGL LAHIR'.ljust(20), 'TEMPAT LAHIR'.ljust(10))
print('-' * 65)

for i in range(len(listBaru)) :
    print(listBaru[i][0].ljust(10), listBaru[i][1].ljust(20), listBaru[i][2].ljust(20), listBaru[i][3].ljust(10),)
