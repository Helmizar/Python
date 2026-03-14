import numpy as np

nama = []
nim = []
nilai = []
tahun = []

n = int(input("Masukkan jumlah mahasiswa: "))

for i in range(n):
    print("Data mahasiswa ke-", i +1)
    nama.append(input("Nama : "))
    nim.append(input("Nim : "))
    nilai.append(float(input("Nilai : ")))
    tahun.append(float(input("Tahun Masuk: ")))

nama = np.array(nama)
nim = np.array(nim)
nilai = np.array(nilai)
tahun = np.array(tahun)

print("\nData Mahasiswa")
for i in range(n):
    print(nama[i], nim[i], nilai[i], tahun[i])

print("\nNilai Tertinggi :", np.max(nilai))
print("Nilai Terendah: ", np.min(nilai))
print("Nilai Rata-rata: ", np.mean(nilai))

cari = input("\nCari mahasiswa (Nama/NIM):")

for i in range(n):
    if cari == nama[i]or cari == nim[i]:
        print("\nData ditemukan: ")
        print("Nama: ", nama[i])
        print("Nim: ", nim[i])
        print("Nilai: ", nilai[i])
        print("Tahun masuk: ", tahun[i])