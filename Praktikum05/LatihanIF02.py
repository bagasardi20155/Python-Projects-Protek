indo = int(input('Masukkan Nilai Bahasa Indonesia : '))

mtk = int(input('Masukkan Nilai Matematika : '))

ipa = int(input('Masukkan Nilai IPA : '))
    
print('===============================')

if(indo < 0 or indo > 100) :
    print('Maaf nilai tidak valid')
    
elif(mtk < 0 or mtk > 100 ) :
    print('Maaf nilai tidak valid')
    
elif(ipa < 0 or ipa > 100) :
    print('Maaf nilai tidak valid')
    
elif(indo>60 and ipa>60 and mtk>70) :
    print('Status Kelulusan : LULUS')
    
else :
     print('Status Kelulusan : Tidak LULUS')
