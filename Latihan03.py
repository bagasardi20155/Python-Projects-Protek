
print('-----------------------------')
print('PROGRAM HITUNG RATA-RATA')
print('-----------------------------')


    
i = True
zigma = 0
jumlah = 0
    
while(i == True):
    try :
            
        bil = int(input("Masukkan bilangan bulat : "))
        zigma += bil
        jumlah += 1
        
        opsi = input("Lagi (y/n)? : ")

        if(opsi == 'y') :
            i = True
            
        elif(opsi == 'n') :
            i = False

        else :
            print('Inputan Invalid')
            break

    except ValueError:
            print('Bukan Bilangan Bulat')
            continue
    
    
rerata = zigma / jumlah

print('Rata-ratanya adalah:', rerata)
    
