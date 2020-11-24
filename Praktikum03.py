try :

    file = open("F:\DOKUMEN KULIAH SMT 1\Pemrograman Terstruktur\Praktikum 7\data1.txt", "r")

    sum = 0
    for data in file:
        
        try :
            sum = sum + int(data)
            
        except ValueError :
            continue
    
    print(sum)
    
except FileNotFoundError :
    print('File tidak ditemukan')
