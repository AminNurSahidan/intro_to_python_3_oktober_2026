# CRUD 
# Create
# Initialitation data
data_makanan = ["Nasi Goreng", "Mie Goreng", "Sate Ayam", "Bakso", "Ayam"]
# Add data (append) 
data_makanan.append("Soto Ayam")
data_makanan.append("Soto Lamongan")
data_makanan.append(["Nasi", "Semangka"])
# Read
print(f"All Data : {data_makanan}")
print(f"Data ke 5 : {data_makanan[5]}")
# Update
data_makanan[7] = "Nasi"
print(f"Al Data : {data_makanan}")
# Delete
del data_makanan[6]
print(f"All Data : {data_makanan}")