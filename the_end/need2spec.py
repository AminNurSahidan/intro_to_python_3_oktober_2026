laptop = [
    {"nama": "Lenovo Thinkpad T14 Gen 4",
     "harga": 10_500_000,
     "cpu": "AMD Ryzen 5 PRO 7540U",
     "gpu": "AMD Radeon 740M",
     "ram": 16,
     "ssd": 512,
     "kebutuhan": ["programming", "desain", "office"]
    },
    {"nama": "HP EliteBook 845 G7",
     "harga": 6_200_000,
     "cpu": "AMD Ryzen 5 PRO 4650U",
     "gpu": "AMD Radeon Graphics Vega 6",
     "ram": 16,
     "ssd": 512,
     "kebutuhan": ["office"]
    },
    {"nama": "Lenovo Thinkpad X1 Extreme G2",
     "harga": 9_500_000,
     "cpu": "Intel Core i5 9400H",
     "gpu": "NVIDIA GeForce GTX 1650 Max-Q 4GB GDDR5",
     "ram": 16,
     "ssd": 512,
     "kebutuhan": ["desain", "office"]
    },
]


def baca_budget(teks):
    teks = teks.lower().replace(" ", "")
    if teks.endswith("juta"):
        return int(float(teks[:-4].replace(",", ".")) * 1_000_000)
    elif teks.endswith("jt"):
        return int(float(teks[:-2].replace(",", ".")) * 1_000_000)
    else:
        return int(teks.replace(".", "").replace(",", ""))


def pilih_kebutuhan():
    print("Kebutuhan Utama :")
    print("1. Programming")
    print("2. Office")
    print("3. Desain")
    pilihan = input("Pilih (1-3): ")

    daftar_kebutuhan = {"1": "programming", "2": "office", "3": "desain"}
    return daftar_kebutuhan[pilihan]

print("=" * 30)
budget = baca_budget(input("Budget berapa? "))

print("=" * 30)
kebutuhan = pilih_kebutuhan()

ketemu = False
print("=" * 30)
print("Laptop yang cocok:")
print()
for item in laptop:
    if item["harga"] <= budget and kebutuhan in item["kebutuhan"]:
        print(f"{item['nama']} (Rp{item['harga']:,})")
        print()
        print("Spesifikasi Laptop :")
        print(f"- CPU : {item['cpu']}")
        print(f"- GPU : {item['gpu']}")
        print(f"- RAM : {item['ram']}GB")
        print(f"- SSD : {item['ssd']}GB")
        print("=" * 30)
        ketemu = True

if not ketemu:
    print("Nggak ada laptop yang cocok, nabung dulu bro!")
