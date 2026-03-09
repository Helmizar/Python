def isKabisat(tahun):
    if (tahun % 400 == 0) or (tahun % 4 == 0 and tahun %100 != 0):
        return True
    else:
        return False
    
#untuk memanggil fungsi
tahun = int(input("masukkan tahun: "))
hasil = isKabisat(tahun)

if hasil:
    print("True - Tahun kabisat")
else:
    print("False - Bukan tahun kabisat")