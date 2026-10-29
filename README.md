Pertemuan 13 - Debugging dan Testing

Nama: Airin Erlikasna Br Perangin Angin
NIM: 2225250196
Kelas: Pendidikan Matematika

Kasus

Pada pertemuan ini, dilakukan debugging pada tiga kesalahan program:

1. Bug rata-rata: Program membagi jumlah nilai dengan angka tetap 5, padahal jumlah data sebenarnya 4.
2. Bug status kelulusan: Nilai 60 dianggap tidak lulus karena menggunakan operator ">".
3. Bug nilai tertinggi: Program menggunakan operator "<", sehingga tidak menemukan nilai tertinggi dengan benar.

Test Case


ID| Input| Expected| Actual Awal| Status
T1| "[80, 60, 90, 70]" rata-rata| "75.0"| "60.0"| PASS
T2| "[100, 80]" rata-rata| "90.0"| Belum diuji sebelum perbaikan| PASS
T3| Nilai "60" untuk status| "Lulus"| "Tidak lulus"| PASS
T4| Nilai "59" untuk status| "Tidak lulus"| Belum diuji sebelum perbaikan| PASS
T5| "[80, 60, 90, 70]" nilai tertinggi| "90"| "0"| PASS

Bug Report

Bug 1: Perhitungan rata-rata

- Penyebab: Pembagian menggunakan angka tetap 5.
- Perbaikan: Menggunakan "len(nilai)" untuk menghitung jumlah data.
- Hasil: Rata-rata menjadi "75.0".

Bug 2: Status kelulusan

- Penyebab: Menggunakan operator "> 60".
- Perbaikan: Mengganti operator menjadi ">= 60".
- Hasil: Nilai 60 dinyatakan lulus.

Bug 3: Nilai tertinggi

- Penyebab: Menggunakan operator "<" dan nilai awal 0.
- Perbaikan: Memulai dari nilai pertama dan menggunakan operator ">".
- Hasil: Nilai tertinggi menjadi "90".

Retest

Setelah perbaikan, program dijalankan kembali dengan input awal.

Hasil pengujian:

Rata-rata: 75.0
Status 60: Lulus
Tertinggi: 90

Ketiga hasil sesuai dengan yang diharapkan untuk input tersebut.

Cara Menjalankan

Jalankan perintah berikut pada terminal VS Code:

python praktik/praktik_4_debugging.py

Refleksi

Saya belajar bahwa debugging digunakan untuk menemukan dan memperbaiki kesalahan program. Tracing membantu memahami perubahan nilai variabel, sedangkan testing digunakan untuk membandingkan hasil aktual dengan hasil yang diharapkan. Setelah memperbaiki bug, program perlu diuji kembali untuk memastikan hasilnya benar.

Kuis Pertemuan 13

1. Perbedaan syntax error, runtime error, dan logical error: Syntax error terjadi karena penulisan kode tidak sesuai aturan, runtime error terjadi ketika program berjalan, sedangkan logical error terjadi ketika program berjalan tetapi hasilnya salah.

2. Fungsi traceback: Menunjukkan informasi kesalahan dan lokasi baris kode yang menyebabkan masalah.

3. Kapan Step Into digunakan? Ketika ingin masuk ke dalam fungsi yang dipanggil dan melihat proses di dalamnya.

4. Perbedaan Step Over dan Step Into: Step Over menjalankan satu baris tanpa masuk ke dalam fungsi, sedangkan Step Into masuk ke dalam fungsi yang dipanggil.

5. Mengapa nilai batas perlu diuji? Untuk memastikan program menangani nilai yang tepat berada pada batas dengan benar.

6. Perbedaan expected result dan actual result: Expected result adalah hasil yang diharapkan, sedangkan actual result adalah hasil yang benar-benar diperoleh dari program.

7. Arti regresi setelah perbaikan: Munculnya kembali kesalahan lama atau munculnya masalah baru setelah perubahan kode.

8. Mengapa debugging diawali dengan reproduksi masalah? Agar kesalahan dapat diamati dan penyebabnya lebih mudah ditelusuri.

9. Mengapa perubahan kode sebaiknya minimal? Agar perbaikan lebih terarah dan mengurangi risiko munculnya kesalahan baru.

10. Manfaat commit khusus bertipe fix pada GitHub: Memudahkan identifikasi perubahan yang bertujuan memperbaiki bug dan memudahkan penelusuran riwayat kode.