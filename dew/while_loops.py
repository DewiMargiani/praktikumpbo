jumlah_angka = int(input("Masukkan jumlah angka yang ingin diuji: "))
counter = 0

while counter < jumlah_angka:
    angka = float(input("Masukkan angka: "))
    
    if angka > 0:
        print("Angka positif.")
    elif angka < 0:
        print("Angka negatif.")
    else:
        print("Nol.")
    
    counter += 1
