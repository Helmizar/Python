import numpy as np

namaBarang = []
kodeBarang = []
jumlah = []
harga = []

n = int(input("Masukkan jumlah barang: "))

for i in range(n):
    print("\nData barang ke-", i+1)
    namaBarang.append(input("Nama Barang : "))
    kodeBarang.append(input("Kode Barang : "))
    jumlah.append(int(input("Jumlah : ")))
    harga.append(float(input("Harga per unit : ")))

namaBarang = np.array(namaBarang)
kodeBarang = np.array(kodeBarang)
jumlah = np.array(jumlah)
harga = np.array(harga)

print("\nData Inventaris")
for i in range(n):
    print(namaBarang[i], kodeBarang[i], jumlah[i], harga[i])

total = jumlah * harga
print("\nTotal nilai setiap barang:")
for i in range(n):
    print(namaBarang[i], "=", total[i])

print("Total seluruh inventaris =", np.sum(total))

cari = input("\nCari barang (Nama / Kode): ")

for i in range(n):
    if cari == namaBarang[i] or cari == kodeBarang[i]:
        print("\nData ditemukan:")
        print("Nama Barang :", namaBarang[i])
        print("Kode Barang :", kodeBarang[i])
        print("Jumlah :", jumlah[i])
        print("Harga :", harga[i])