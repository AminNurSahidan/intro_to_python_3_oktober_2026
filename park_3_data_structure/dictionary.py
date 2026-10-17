# Inisialisasi dictionary
data_kelas = {
    "nama_ketua" : "Tono",
    "jurusan_kelas" : ["IPA", "IPS", "Bahasa"],
    "tingkat_kelas" : 12,
}
# Read
print(f"Data All : {data_kelas}")
print(f"Nama Ketua Kelas : {data_kelas["nama_ketua"]}")
print(f"Jurusan Kelas : {data_kelas["jurusan_kelas"][1]}")

# Update
data_kelas["jurusan_kelas"] = "IPS"
print(f"Data All : {data_kelas}")

# Delete
del data_kelas["nama_ketua"]
print(f"Data All : {data_kelas}")
# Append Data
data_kelas["nama_ketua"] = "Budi"
print(f"Data All : {data_kelas}")
print(f"Nama Ketua Kelas : {data_kelas["nama_ketua"]}")