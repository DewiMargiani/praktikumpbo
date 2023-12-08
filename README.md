# tugas1pbo
Nama : Dewi Margiani
NPM  : G1F022037

## 1. Buatlah perulangan hingga 100 menggunakan python dengan output yang ditentukan
### Source Code
<img width="460" alt="perulangan " src="https://github.com/DewiMargiani/praktikumpbo/assets/150019055/d798298a-f116-4697-9fdd-f4fc623b38bd">

### Penjelasan Source Code

Kode Python di atas adalah fungsi main() yang menerima satu argumen berupa nama. Fungsi ini akan menghasilkan output seperti yang ditunjukkan dalam gambar.
Fungsi ini terdiri dari dua bagian utama:
a) Bagian pertama adalah deklarasi variabel _output_. Variabel ini akan digunakan untuk menyimpan output dari fungsi.
b) Bagian kedua adalah perulangan for. Perulangan ini akan iterasi dari 1 hingga 100.
Pada setiap iterasi, kode akan memeriksa apakah nilai i habis dibagi 10. Jika demikian, kode akan mencetak nama yang diberikan sebanyak tiga kali. Jika tidak, kode akan mencetak nilai i.

_def main(name)_: Baris kode ini mendefinisikan fungsi main(). Fungsi ini menerima satu argumen berupa nama dan mengembalikan string yang berisi output.

_for i in range(1, 101)_: kode ini memulai perulangan for. Perulangan ini akan iterasi dari 1 hingga 100.

_if i % 10 == 0:
  output += f"{name}\n" * 3_ , kode ini memeriksa apakah nilai i habis dibagi 10. Jika demikian, kode akan mencetak nama yang diberikan sebanyak tiga kali.

_else:
  output += str(i) + "\n"_ ,  kode ini akan mencetak nilai i.

_return output_ kode ini mengembalikan string yang berisi output.
### Screenshot Output
<img width="151" alt="perulangan1" src="https://github.com/DewiMargiani/praktikumpbo/assets/150019055/b73b4c28-533b-4ec0-a965-f55641d5deed">
<img width="146" alt="perulangan2" src="https://github.com/DewiMargiani/praktikumpbo/assets/150019055/d762f332-ed28-4ade-af5a-21d173dd66ff">
<img width="152" alt="perulangan3" src="https://github.com/DewiMargiani/praktikumpbo/assets/150019055/02f7e1f8-d9be-4d68-864f-4c0fe956d190">

## 2. Buatlah program bebas, dengan menerapkan if else pada:
  a. For Loops
  b. While Loops
### Source Code For Loops
<img width="395" alt="forloops" src="https://github.com/DewiMargiani/praktikumpbo/assets/150019055/850723af-431c-4ff6-9241-c250a4fc45cc">

### Penjelasan Code
Kode Python di atas adalah program yang akan meminta pengguna untuk memasukkan jumlah angka yang ingin diuji. Kemudian, program akan meminta pengguna untuk memasukkan angka tersebut satu per satu. Setelah itu, program akan menentukan apakah angka tersebut positif, negatif, atau nol.

_jumlah_angka = int(input("Masukkan jumlah angka yang ingin diuji: "))_ kode ini meminta pengguna untuk memasukkan jumlah angka yang ingin diuji. Input dari pengguna akan disimpan ke dalam variabel _jumlah_angka_.

_for _ in range(jumlah_angka):_ kode ini memulai perulangan _for_. Perulangan ini akan iterasi sebanyak _jumlah_angka_ kali.

_angka = float(input("Masukkan angka: "))_ kode ini meminta pengguna untuk memasukkan angka. Input dari pengguna akan disimpan ke dalam variabel _angka_.

_if angka > 0:
  print("Angka positif.")_ kode ini memeriksa apakah nilai angka lebih besar dari 0. Jika demikian, kode akan mencetak _"Angka positif."_

_elif angka < 0:
  print("Angka negatif.")_ kode ini memeriksa apakah nilai angka lebih kecil dari 0. Jika demikian, kode akan mencetak _"Angka negatif."_ 

_else:
  print("Nol.")_ kode ini akan mencetak _"Nol"_ jika nilai angka sama dengan 0.
### Screenshot Output
<img width="226" alt="hasilfor" src="https://github.com/DewiMargiani/praktikumpbo/assets/150019055/d22e8415-6aae-49e0-a58a-2b578d796f5f">
Pada contoh ini, pengguna memasukkan 2 angka, yaitu 5, -5. Oleh karena itu, program akan menghasilkan output seperti yang ditunjukkan di atas.

### Source Code While Loops
<img width="398" alt="whileloops" src="https://github.com/DewiMargiani/praktikumpbo/assets/150019055/8c1ee670-bb18-4b66-8e8c-d81ad9258019">

### Penjelasan Code
Kode Python di atas adalah program yang akan meminta pengguna untuk memasukkan jumlah angka yang ingin diuji. Kemudian, program akan meminta pengguna untuk memasukkan angka tersebut satu per satu. Setelah itu, program akan menentukan apakah angka tersebut positif, negatif, atau nol.

Kode ini memiliki dua bagian utama:

a) Bagian pertama adalah deklarasi variabel jumlah_angka dan counter. Variabel jumlah_angka akan menyimpan jumlah angka yang ingin diuji, dan variabel counter akan digunakan untuk melacak iterasi saat ini dari perulangan while.
b) Bagian kedua adalah perulangan while. Perulangan ini akan terus berjalan selama nilai counter kurang dari jumlah_angka.
Pada setiap iterasi, kode akan meminta pengguna untuk memasukkan angka. Input dari pengguna akan disimpan ke dalam variabel angka. Kemudian, kode akan memeriksa apakah angka tersebut positif, negatif, atau nol.

Berikut adalah penjelasan baris kode secara lebih rinci:

_jumlah_angka = int(input("Masukkan jumlah angka yang ingin diuji: "))_ kode ini meminta pengguna untuk memasukkan jumlah angka yang ingin diuji. Input dari pengguna akan disimpan ke dalam variabel _jumlah_angka_.

_counter = 0_ kode ini menginisialisasi variabel counter ke nilai _0_.

_while counter < jumlah_angka:_ kode ini memulai perulangan while. Perulangan ini akan terus berjalan selama nilai counter kurang dari _jumlah_angka_.

_angka = float(input("Masukkan angka: "))_ kode ini meminta pengguna untuk memasukkan angka. Input dari pengguna akan disimpan ke dalam variabel _angka_.

_if angka > 0:
  print("Angka positif.")_  kode ini memeriksa apakah nilai angka lebih besar dari 0. Jika demikian, kode akan mencetak _"Angka positif."_

_elif angka < 0:
  print("Angka negatif.")_ kode ini memeriksa apakah nilai angka lebih kecil dari 0. Jika demikian, kode akan mencetak _"Angka negatif."_

_else:
  print("Nol.")_ kode ini akan mencetak _"Nol"_ jika nilai angka sama dengan 0.

_counter += 1_ kode ini menambah nilai _counter_ sebesar 1.

Perbedaan antara kode ini dengan kode sebelumnya adalah penggunaan perulangan _while_. Perulangan _while_ akan terus berjalan selama kondisi yang diberikan terpenuhi. Dalam hal ini, kondisi yang diberikan adalah nilai _counter_ kurang dari _jumlah_angka_.
### Screenshot Output
<img width="212" alt="hasilwhile" src="https://github.com/DewiMargiani/praktikumpbo/assets/150019055/cdd828b2-6576-4b0a-a83f-e9a0ec23e50a">

## 3. Buatlah sebuah variabel dengan tipe data array, kemudian tampilkan semua nilai dalam variabel tersebut menggunakan perulangan for
### Source Code
<img width="398" alt="3" src="https://github.com/DewiMargiani/praktikumpbo/assets/150019055/5f343385-3148-4bc6-b90c-ffb65307739e">

### Penjelasan Source Code
Kode Python di atas adalah program yang akan membuat variabel dengan tipe data array dan menampilkan semua nilai dalam variabel menggunakan perulangan for.

Berikut adalah penjelasan baris kode secara lebih rinci:
_my_array = [10, 20, 30, 40, 50]_ kode ini membuat variabel my_array dengan tipe data array. Nilai-nilai dalam variabel my_array adalah _10, 20, 30, 40, dan 50_.

_for value in my_array:_ kode ini memulai perulangan for. Perulangan ini akan iterasi sebanyak jumlah nilai dalam variabel _my_array_.

_print(value)_ kode ini mencetak nilai _value_ pada setiap iterasi.
### Screenshot Output
<img width="53" alt="3,2" src="https://github.com/DewiMargiani/praktikumpbo/assets/150019055/f966732f-230a-4fb2-bfc0-d7cca43a3f7c">

Pada contoh ini, variabel _my_array_ berisi lima nilai. Oleh karena itu, perulangan _for_ akan iterasi sebanyak lima kali. Pada setiap program, nilai _value_ akan berganti sesuai dengan nilai pada indeks program saat ini.
