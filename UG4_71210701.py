import json

# Inputan dari pengguna
hsl_barang = int(input("Masukkan jumlah barang = "))

barng = []
hsl = 0

# Menerima input loop dari nama dan harga barang
for i in range(hsl_barang):

    nama_barang = input(f"Nama barang {i+1} = ")
    h_barang = int(input(f"Harga barang {i+1} = "))
    
    # Menambah data barang ke list barang
    barng.append({'nama': nama_barang, 'harga': h_barang})
    
    # Menambahkan harga barang ke dalam total
    hsl += h_barang

# Membuat dictionary untuk data yang akan disimpan ke dalam file JSON
dat = {'hsl': hsl, 'barang': barng}

# Data disimpan ke dalam file JSON
with open('data_barang.json', 'w') as file:
    json.dump(dat, file)

print("Data telah disimpan ke dalam file data_barang.json")