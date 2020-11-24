
try :
    file = input('Masukkan nama file : ')

    print('Isi file', file, 'adalah : ')
    print(open(file, 'r').read())

except FileNotFoundError:
    print('File tidak ditemukan')

except UnicodeDecodeError:
    print('File tidak bisa dibuka')


'''
#support docx file

import docx2txt

try :
    file = input('Masukkan nama file : ')

    fileSplit = file.split(".")
    
    if(fileSplit[1] == "docx"):
        
        isiFile = docx2txt.process(file)
        print(isiFile)

    else :
        print(open(file, 'r').read())
        
    
except FileNotFoundError:
    print('File tidak ditemukan')

except UnicodeDecodeError:
    print('File tidak bisa dibuka')
'''
