# README Praktikum Penanganan Eksepsi dan File Handling

Dokumen ini berisi penjelasan lengkap untuk setiap percobaan dan latihan dari modul praktikum **Penanganan Eksepsi dalam Python**.

---

## ## **Percobaan 1 – Mengamati Runtime Error**

### **Tujuan:**

Mengamati bagaimana error *runtime* terjadi tanpa penanganan, sehingga program berhenti mendadak.

### **Penjelasan Program:**

Program meminta dua input angka kemudian melakukan pembagian. Jika pembagi bernilai 0, program menghasilkan **ZeroDivisionError** dan berhenti.

### **Inti Pembelajaran:**

* Program *crash* tanpa `try-except`.
* *Runtime error* berbeda dengan *syntax error*.

---

## **Percobaan 2 – Penanganan Error Sederhana (try-except)**

### **Tujuan:**

Mencegah program berhenti ketika terjadi error pembagian dengan nol.

### **Penjelasan Program:**

`try` digunakan untuk menjalankan kode yang berpotensi menyebabkan error. Jika terjadi **ZeroDivisionError**, program tidak berhenti, tetapi menampilkan pesan ramah.

### **Inti Pembelajaran:**

* `try-except` dapat mencegah program berhenti tiba-tiba.
* Error dapat ditangani lebih baik oleh programmer.

---

## **Percobaan 3 – Menangani Banyak Jenis Eksepsi**

### **Tujuan:**

Menangani lebih dari satu jenis error dalam satu blok kode.

### **Penjelasan Program:**

Program meminta input angka, lalu membagi 10 dengan angka tersebut. Menggunakan beberapa `except`:

* `ValueError` → input bukan angka
* `ZeroDivisionError` → input 0
* `Exception` → error lain yang tidak terduga

### **Inti Pembelajaran:**

* Dapat menangani berbagai error secara spesifik.
* `Exception` digunakan sebagai *catch-all*.

---

## **Percobaan 4 – Penggunaan else dan finally**

### **Tujuan:**

Memahami fungsi `else` dan `finally` dalam blok eksepsi.

### **Penjelasan Program:**

* Blok `else` berjalan jika **tidak ada error**.
* Blok `finally` berjalan **selalu**, baik ada error maupun tidak.

### **Inti Pembelajaran:**

* `else` untuk kode yang aman dieksekusi setelah `try`.
* `finally` cocok untuk menutup file, koneksi, atau pesan akhir.

---

## **Percobaan 5 – Mengakses Objek Eksepsi (`as e`)**

### **Tujuan:**

Menampilkan pesan error asli dari Python menggunakan variabel error.

### **Penjelasan Program:**

Saat terjadi error, seperti `IndexError` atau `ValueError`, pesan error asli disimpan di variabel `e`.

### **Inti Pembelajaran:**

* Menampilkan informasi error yang lebih lengkap.
* Membantu debugging program.

---

## **Percobaan 6 – Memicu Eksepsi Sendiri (raise)**

### **Tujuan:**

Mempraktikkan cara membuat error sesuai kebutuhan.

### **Penjelasan Program:**

Jika nilai level kurang dari 1, program memicu error menggunakan `raise ValueError()`.

### **Inti Pembelajaran:**

* `raise` digunakan untuk validasi.
* Error dapat dipicu secara manual.

---

# **Latihan 1 – Kalkulator Aman**

### **Tujuan:**

Menerapkan semua konsep eksepsi pada program kalkulator.

### **Fitur Program:**

✔ Menangani input bukan angka (`ValueError`)
✔ Menangani pembagian dengan nol (`ZeroDivisionError`)
✔ Operator salah memicu `raise Exception`
✔ Program tidak berhenti meskipun terjadi error

### **Inti Pembelajaran:**

* Menggabungkan logika aritmatika dengan exception handling yang lengkap.
* Membuat program lebih aman digunakan.

---

# **Latihan 2 – Validasi Daftar Nilai**

### **Tujuan:**

Memproses list campuran angka dan teks tanpa membuat program error.

### **Penjelasan Program:**

Program membaca setiap elemen list dan mencoba mengubahnya menjadi angka. Jika gagal, error ditangkap dan data dilewati.

### **Inti Pembelajaran:**

* `try-except` **di dalam loop**.
* Program **tetap berjalan meskipun ada data salah**.
* Menghitung rata-rata hanya dari data valid.

---

## **Kesimpulan Akhir**

Pada praktikum ini, mahasiswa mempelajari:

1. Perbedaan error runtime dan syntax error.
2. Penanganan error menggunakan `try-except`.
3. Penggunaan `else`, `finally`, dan `raise`.
4. Penanganan banyak jenis error.
5. Teknik melewati error dalam loop.
6. Penerapan exception handling pada studi kasus nyata.

---

Jika ingin, saya bisa membuatkan **versi PDF**, **versi laporan resmi**, atau **menambahkan screenshot input-output**.
