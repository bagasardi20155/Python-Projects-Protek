file = open('dataMhs.txt', 'r')

baris = file.readlines()

dicti = {}

for i in range(len(baris)) :
    a = baris[i].split('|')
    a[2] = a[2].replace('\n', '')
    
    dicti[i] = {'nama' : a[0], 'nim' : a[1], 'alamat' : a[2]}

print(dicti)

    