nilai = [{'nim' : 'A01', 'nama' : 'Agustina', 'mid' : 50, 'uas' : 80},
         {'nim' : 'A02', 'nama' : 'Budi', 'mid' : 40, 'uas' : 90}, 
         {'nim' : 'A03', 'nama' : 'Chicha', 'mid' : 100, 'uas' : 50}, 
         {'nim' : 'A04', 'nama' : 'Donna', 'mid' : 20, 'uas' : 100},
         {'nim' : 'A05', 'nama' : 'Fatimah', 'mid' : 70, 'uas' : 100}]


print("=" * 61)
print("NIM".ljust(8), "NAMA".ljust(8),  "N.MID".rjust(8),  "N.UAS".rjust(8), "N.AKHIR".rjust(10),  "STATUS".rjust(10))
print("-" * 61)


for x in nilai :
    
    nilaiAkhir = (x['mid'] + (2 * x['uas'])) / 3
    nilaiAkhir = int(nilaiAkhir)

    if(nilaiAkhir >= 60) :
        status = "LULUS"
    else :
        status = "TIDAK LULUS"

    print(x['nim'].ljust(8),   x['nama'].ljust(8),   str(x['mid']).rjust(8),   str(x['uas']).rjust(8), str(nilaiAkhir).rjust(8),  status.rjust(12))

print("-" * 61)
