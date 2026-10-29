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

B01 — Perhitungan Rata-rata

- Gejala: Rata-rata yang dihasilkan adalah 60.0, padahal seharusnya 75.0.
- Test case: T1.
- Lokasi: "praktik/praktik_4_debugging.py", fungsi "hitung_rata_rata()".
- Akar penyebab: Pembagi rata-rata tidak sesuai dengan jumlah data.
- Perbaikan: Mengganti pembagi dengan "len(nilai)" dan menambahkan pemeriksaan jika data kosong.
- Retest: PASS — rata-rata data "[80, 60, 90, 70]" menjadi 75.0.

B02 — Batas Kelulusan

- Gejala: Nilai 60 dinyatakan tidak lulus, padahal seharusnya lulus.
- Test case: T3.
- Lokasi: "praktik/praktik_4_debugging.py", fungsi "status()".
- Akar penyebab: Kondisi menggunakan "nilai > 60", sehingga nilai 60 tidak termasuk lulus.
- Perbaikan: Mengubah kondisi menjadi "nilai >= 60".
- Retest: PASS — nilai 60 dinyatakan Lulus dan nilai 59 dinyatakan Tidak lulus.

B03 — Nilai Tertinggi

- Gejala: Program menghasilkan nilai tertinggi 0, bukan 90.
- Test case: T5.
- Lokasi: "praktik/praktik_4_debugging.py", fungsi "nilai_tertinggi()".
- Akar penyebab: Perbandingan menggunakan operator "<", sehingga pencarian nilai tertinggi tidak berjalan dengan benar.
- Perbaikan: Memulai nilai tertinggi dari elemen pertama dan menggunakan operator ">".
- Retest: PASS — nilai tertinggi dari "[80, 60, 90, 70]" adalah 90

Retest

Semua test case telah dijalankan kembali setelah perbaikan.

ID| Hasil yang Diharapkan| Hasil Aktual Setelah Perbaikan| Status
T1| Rata-rata 75.0| 75.0| PASS
T2| Rata-rata 90.0| 90.0| PASS
T3| Lulus| Lulus| PASS
T4| Tidak lulus| Tidak lulus| PASS
T5| Nilai tertinggi 90| 90| PASS

Tidak ditemukan kegagalan pada kelima test case setelah perbaikan.

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