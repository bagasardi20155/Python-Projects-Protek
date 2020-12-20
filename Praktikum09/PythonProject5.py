nilai = [{'nim' : 'A01', 'nama' : 'Agustina', 'mid' : 50, 'uas' : 80},
         {'nim' : 'A02', 'nama' : 'Budi', 'mid' : 40, 'uas' : 90}, 
         {'nim' : 'A03', 'nama' : 'Chicha', 'mid' : 100, 'uas' : 50}, 
         {'nim' : 'A04', 'nama' : 'Donna', 'mid' : 20, 'uas' : 100},
         {'nim' : 'A05', 'nama' : 'Fatimah', 'mid' : 70, 'uas' : 100}]

print("=" * 41)
print("NIM".ljust(8), "NAMA".ljust(8),  "N.MID".rjust(8),  "N.UAS".rjust(8))
print("-" * 41)

for x in  nilai :
    print(x['nim'].ljust(8),   x['nama'].ljust(8),   str(x['mid']).rjust(8),   str(x['uas']).rjust(8))
