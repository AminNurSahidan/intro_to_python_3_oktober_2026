laptop = [
    {"nama": "Lenovo Thinkpad T14 Gen 4",
     "harga": 10_500_000,
     "cpu": "AMD Ryzen 5 PRO 7540U",
     "gpu": "AMD Radeon 740M",
     "ram": 16,
     "ssd": 512,
     "kebutuhan": ["programming", "desain"]
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

open_file = open("./data_laptop.txt","w")
open_file.write(str(laptop))
open_file.close()