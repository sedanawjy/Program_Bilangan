# Program_Bilangan
Program ini dibuat untuk memenuhi persyaratan seleksi awal program Magang Bersertifikat di Studycle

# Kriteria Program
- Program dapat menerima input beberapa bilangan
- Program memiliki fungsi untuk mengurutkan semua bilangan yang dimasukkan dari yang terkecil sampai yang terbesar
- Program dapat menampilkan keluaran yang mencakup: nilai rata-rata, nilai tengah dan hasil perkalian dari semua bilangan yang dimasukkan
- Format input/output bebas
- Bahasa pemrograman yang dapat digunakan bebas
- Spesifikasi lain dapat diasumsikan secara bebas

# Implementasi
1. Input user dapat menggunakan tombol button maupun mengisi kolom inputan. 
2. Penulis menggunakan fungsi bawaan dari Python untuk mengurutkan bilangan terkecil sampai yang terbesar.
3. Logika mencari rata-rata adalah penjumlahan seluruh bilangan input dibagi dengan jumlah inputan user. 
4. Mencari nilai tengah adalah dengan membagi jumlah inputan user dengan 2, dibulatkan ke bawah untuk mendapatkan index tengah. Index tersebut di modulo dua. agar dapat menentukan apakah terdapat dua titik tengah atau hanya satu. Jika terdapat dua titik tengah maka kedua bilangan tersebut ditambah lalu dibagi dengan dua.
5. Hasil perkalian didapatkan dengan melakukan looping terhadap seluruh input dan mengalikannya.

# Alur Program
- Tampilan program.
![image](https://user-images.githubusercontent.com/56629564/126279532-5d4103e7-d7b6-4d92-a93d-188c1101b943.png)
User dapat mengklik tombol button maupun mengetik pada kolom dengan lingkaran merah untuk memilih angka inputan lalu mengklik tombol Submit. Tombol C digunakan jika user ingin mereset angka inputan jika terdapat kesalahan.
- Hasil program.
![image](https://user-images.githubusercontent.com/56629564/126279857-4f505813-bbd9-4dc7-9a98-6c691a89c7f2.png)
Setelah user mengklik tombol Submit, hasil pertama akan langsung keluar seperti pada gambar di atas.
![image](https://user-images.githubusercontent.com/56629564/126280018-69b25341-caa6-4540-8868-6e6f94ae063d.png)
Hasil akan berubah-ubah menyesuaikan setiap kali user menginputkan bilangan dan mengklik tombol Submit.
- Keluar Program
![image](https://user-images.githubusercontent.com/56629564/126280919-b58d02eb-11b0-4e17-84da-508175b7df60.png)
User dapat keluar dari program dengan cara mengklik tombol X di sebelah kanan atas.

# Batasan Program
- Program tidak dapat menginput bilangan desimal.
- Program tidak menampilkan error ke user.
- Program tidak memiliki fitur menghapus seluruh input.
- Tampilan program terbatas dengan default dari library Tkinter.
- Code belum dibagi menjadi beberapa modul.

# Dokumentasi Code
1. Input user terdapat pada baris 32 & 33, serta baris 91 - 105.
![image](https://user-images.githubusercontent.com/56629564/126282106-c5ef620a-291c-4d44-b2a6-1934b6056db7.png)
![image](https://user-images.githubusercontent.com/56629564/126282046-0081dc52-f80b-4885-8e1f-7d290861bfdc.png)
2. Pengurutan bilangan terdapat pada fungsi urut_bil().
![image](https://user-images.githubusercontent.com/56629564/126282226-d00793b1-7587-47a1-98c0-44b0da563dd3.png)
3. Perhitungan rata-rata bilangan terdapat pada fungsi rata_bil().
![image](https://user-images.githubusercontent.com/56629564/126282320-48c4007a-d14f-44b3-89b8-2eaa7c1d41c2.png)
4. Perhitungan mencari nilai tengah terdapat pada fungsi median_bil().
![image](https://user-images.githubusercontent.com/56629564/126282447-cb209478-10b6-4985-9015-61a16abaf17b.png)
5. Perhitungan mencari hasil perkalian seluruh input user terdapat pada fungsi kali_bil().
![image](https://user-images.githubusercontent.com/56629564/126282530-1fd8e81a-06b0-45bd-a062-3fb4627354df.png)
6. Berikut adalah fungsi untuk mengatur layar inputan.
![image](https://user-images.githubusercontent.com/56629564/126282636-aaaef3be-22f4-4d81-be7d-e917a95c35de.png)
7. Output program didapatkan dengan memanggil fungsi submit().
![image](https://user-images.githubusercontent.com/56629564/126282701-d817e042-4b20-4519-9ff3-75e04d7a379a.png)

Sekian dan terima kasih telah membaca. Have a good day! :)
