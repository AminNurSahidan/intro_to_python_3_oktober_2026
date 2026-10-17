point = (5, 10)
print(point[0]) # 5
print(point[1]) # 10

# Untuk data yang tidak berubah
tanggal_lahir = (30, 11, 2004) # Tanggal, Bulan, Tahun
print("Tanggal lahir : ", tanggal_lahir)

# Iterasi di Tuple
for e in tanggal_lahir:
    print(e)


# Iterasi di Tuple dengan Index
for i in range(len(tanggal_lahir)):
    print(tanggal_lahir[i])