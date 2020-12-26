file = open('angkaDijumlah.txt', 'r')


result = []
for i in file.readlines() :
    
    if('\n' in i) :
        
        replaced = i.replace('\n','')
        splitted = replaced.split('|')
        valueList = int(splitted[0]) + int(splitted[1])
        result.append(valueList)
        
    else :
        
        splitted = i.split('|')
        valueList = int(splitted[0]) + int(splitted[1])
        result.append(valueList)

file.close()

output = open('hasilAngkaDijumlah.txt', 'w')

for i in range(len(result)) :
    output.write(str(result[i]) + '\n')

output.close()
print("Silahkan lihat hasil penjumlahan di hasilAngkaDijumlah.txt")
