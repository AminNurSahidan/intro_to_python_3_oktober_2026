# For
# index sementara in data :
    # nilai yang mau di ulang
# Range(Start, Stop, Step)
print("=====For Loop=====")
for value in range(1, 11):
    print(f"Value ke : {value}")

# yang di loop list
print("=====For Loop using list=====")
makanan = ['Nasi Goreng', 'Mie Goreng', 'Sate Ayam', 'Bakso', 'Ayam', 'Soto Ayam', 'Soto Lamongan', 'Nasi']
for value in makanan:
    print(f"Makanan : {value}")

# While loop
# Saat kita tau kapan kita berhenti tapi tau jalan atau start nya di mana
nomor = 1
while nomor <= 10:
    print(f"Index of : {nomor}")
    nomor += 1

print("=====Break and Continue=====")
nomor = 1
while nomor <= 100:
    if nomor % 2 == 0:
        nomor += 1
        continue
    if nomor >= 20:
        nomor += 1
        break
    print(f"Index of {nomor}")
    nomor += 1