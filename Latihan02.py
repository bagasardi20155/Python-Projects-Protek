import os  

try :
    
    file = input("Masukkan nama file : ")

    if os.path.exists(file) :
        mode = 'a'
    else:
        mode = 'r'
        
    isiFile = open(file, mode)

    lanjut = True
    while(lanjut==True) :
        
        data = input("Data yang mau ditambahkan : ")
        isiFile.write(' ' + data)

        opsi = input('Mau lagi ? (y/n) : ')
        
        if(opsi=='y') :
            lanjut = True
            
        elif(opsi=='n') :
            lanjut = False

        else :
            print('Inputan Invalid')
            break
        
    isiFile.close()

except FileNotFoundError :
    print('File Tidak Ditemukan')

        
        
