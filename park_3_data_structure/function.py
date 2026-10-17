data_karyawan = [
    {
        "nama" : "ibnu",
        "tanggal_lahir" : "2001",
        "gaji" : 8000000,
    },
    {
        "nama" : "rehan",
        "tanggal_lahir" : "2002",
        "gaji" : 7000000,
    },
    {
        "nama" : "bima",
        "tanggal_lahir" : "2003",
        "gaji" : 7500000,
    },
    {
        "nama" : "gondrong",
        "tanggal_lahir" : "2004",
        "gaji" : 6200000,
    },
]

# Void
def template_print(nama, gaji, usia = 30):
    print(f"Nama : {nama}")
    print(f"Gaji : {gaji}")
    print(f"Usia : {usia} Tahun")
    print("========================")

# Non Void
def rumus_usia(tahun_lahir:int):
    tahun_sekarang = 2026
    usia =  tahun_sekarang - int(tahun_lahir)
    return usia

data_karyawan[0]["usia"] = rumus_usia(data_karyawan[0]["tanggal_lahir"])
data_karyawan[1]["usia"] = rumus_usia(data_karyawan[1]["tanggal_lahir"])
data_karyawan[2]["usia"] = rumus_usia(data_karyawan[2]["tanggal_lahir"])
data_karyawan[3]["usia"] = rumus_usia(data_karyawan[3]["tanggal_lahir"])

print("=====Data Karyawan======")
template_print(data_karyawan[0]["nama"],data_karyawan[0]["gaji"],data_karyawan[0]["usia"])
template_print(data_karyawan[1]["nama"],data_karyawan[1]["gaji"],data_karyawan[1]["usia"])
template_print(data_karyawan[2]["nama"],data_karyawan[2]["gaji"],data_karyawan[2]["usia"])
template_print(data_karyawan[3]["nama"],data_karyawan[3]["gaji"],data_karyawan[3]["usia"])