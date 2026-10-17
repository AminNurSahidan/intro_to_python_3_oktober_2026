print("=====if else=====")
nilai = 70

if nilai > 70:
    print("Kamu lulus")
else:
    print("Kamu tidak lulus")

print("=====if elif else======")
nilai = 75

if nilai > 90:
    print("Kamu lulus dengan predikat A")
elif nilai > 80 and nilai >= 90:
    print("Kamu lulus dengan predikat B")
elif nilai > 70 and nilai >= 80:
    print("Kamu lulus dengan predikat C")
elif nilai > 60 and nilai >= 70:
    print("Kamu lulus dengan predikat D")
else:
    print("Kamu Drop Out")

print("=====Match and Case=====")
print("=====Menu=====")
print("1. Menu 1")
print("2. Menu 2")
print("3. Exit")
select = input("Pilih menu : ")
match select:
    case "1":
        print("Kamu memilih menu 1")
    case "2":
        print("Kamu memilih menu 2")
    case "3":
        print("Kamu memilih menu exit")
    case _:
        print("Menut tidak tersedia")

print("===Try and Catch===")
try:
    angka = int(input("Masukkan Angka : "))
    print(f"Angkat yang kamu masukkan adalah {angka}")
except ValueError:
    print("Kamu harus memasukkan angka")
