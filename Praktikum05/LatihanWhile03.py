#Program untuk menampilkan bilangan bulat 0 - 100 yang ganjil

i = 1
jml = 0
sum = 0

while(i <= 100) :
    print(str(i) + '\n')
    sum = sum + i
    i = i + 2
    jml = jml + 1
    

print('Banyaknya Bilangan Ganjil : ' + str(jml))
print('Hasil Penjumlahannya adalah : ' + str(sum))


#dengan for

'''
for i in range(100) :
    if ( i % 2 == 1 ) :
        print(str(i) + '\n')
        sum = sum + i
        i = i + 1
        jml = jml + 1

print('Banyaknya Bilangan Ganjil : ' + str(jml))
print('Hasil Penjumlahannya adalah : ' + str(sum))
    
'''
