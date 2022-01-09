print("="*25)
print("Ulul Rahmawati Putri")
print("5200411013")
print("RoundRobin")

print("="*25)
#input
progone     = str(input("Input nama Program pertama : "))
FirstTime   = int(input("input Waktu Program pertama : "))
progtwo     = str(input("Input nama Program kedua : "))
SecondTime  = int(input("Input waktu Program kedua : "))
progthree   = str(input("Input nama Program ketiga : "))
ThreeTime   = int(input("Input waktu Program ketiga : "))
q           = int(input("Quantum Time / Jatah waktu : "))

urutan = [FirstTime, SecondTime, ThreeTime]

print("="*25)
print("====HASIL Ouput====")
print("Nama Program Satu :", progone,"dan Lama Waktu Program 1 :",FirstTime)
print("Nama Program Dua :", progtwo,"dan Lama Waktu Program 2 :",SecondTime)
print("Nama Program Tiga :", progthree,"dan Lama Waktu Program 3 :",ThreeTime)
print("Lama Waktu Program satu-tiga =",urutan)
print("Quantum Time / Jatah Waktu :",q)
print("List RoundRobinnya adalah")
if FirstTime>SecondTime and SecondTime>ThreeTime:
        if SecondTime>ThreeTime:
            print(FirstTime, SecondTime, ThreeTime)
        else:
            print(FirstTime, ThreeTime,  SecondTime)
elif SecondTime>FirstTime and SecondTime>ThreeTime:
        if FirstTime>ThreeTime:
            print(SecondTime, FirstTime, ThreeTime)
        else:
            print(SecondTime, ThreeTime, FirstTime)
else:
        if FirstTime>SecondTime:
            print(ThreeTime, FirstTime, SecondTime)
        else:
            print(ThreeTime, SecondTime, FirstTime)
