jumlah_angka = int(input("Masukkan jumlah angka yang ingin diuji: "))

for _ in range(jumlah_angka):
    angka = float(input("Masukkan angka: "))
    
    if angka > 0:
        print("Angka positif.")
    elif angka < 0:
        print("Angka negatif.")
    else:
        print("Nol.")
