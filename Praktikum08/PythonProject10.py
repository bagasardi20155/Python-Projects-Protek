buah = {'apel' : 5000,
           'jeruk' : 8500,
           'mangga' : 7800,
           'duku' : 6500}

def jumlahBuah() :
    
    jumlah = int(input("Berapa Kg : ")) 
    harga = buah.get(namaBuah, 0)*jumlah
    return harga


print("Daftar Buah : ")

for x,y in buah.items() :
    print("- ", x, ": ", y)

total = []
lanjut = True
    
while(lanjut==True) :
        
    namaBuah = input("\nNama buah yang dibeli : ").lower()
        
    if(namaBuah not in buah.keys()) :
        print("Maaf, buah yang anda masukkan tidak ada")
        continue
                  
    else :
        try :
            harga = jumlahBuah()
            total.append(harga)
                
            opsi = input("Beli buah yang lain (y/n) ? ").lower()
            if(opsi=='y') :
                lanjut = True
                
            elif(opsi=='n') :
                lanjut = False

            else :
                print('Inputan Invalid')
                break
            
        except ValueError :
                print('\nInputan Invalid Silakan Ulangi')
                continue
    
       

print("-------------------------------------------")
print("Total Harga : ", sum(total))

