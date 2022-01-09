print("="*25)
print("5200411013")
print("Ulul Rahmawati Putri")
print("soal 1")

#INPUT
blok = 2

print("="*25)
ram = int(input("Kapasitas Ram : "))
petabit = int(input("kapasitas petabit : " ))
ramOS   = int(input("Kapasitas ramOS (KBps):"))
proone =int(input("kapasitas proone (kbPS): "))
protwo=int(input("kapasitas protwo (KBps): "))

#rumus
peta = (ram / petabit)
totram =(ramOS + proone + protwo) 
OsRam = (ram-ramOS-proone-protwo) 
alOne = (proone + protwo)/peta

print("="*25)
print("jumlah ram: ",ram)
print("jumlah petabit :", petabit)
print("Kappertabit : ", petabit)
print("Jumlah RAm yang digunakan: ", totram)
print("jumlah RAm yang tidak digunakan : ", OsRam)
print("Total keseluruhan blok yang bervalue 1 :", alOne)
print("Total keseluruhan blok yang bervalue o :", blok - alOne)