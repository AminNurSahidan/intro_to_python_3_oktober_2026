n = int(input("Masukkan Angka : "))
sisa = n % 2
if sisa == 0:
    print("Genap")
else:
    print("Ganjil")

n = int(input("Masukkan Angka cik : "))
i = 1
total = 0
while i <= n:
    total = total + i
    i = i + 1
print(total)