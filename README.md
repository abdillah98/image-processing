# Image Processing Lab

Project ini merupakan lingkungan eksperimen sederhana untuk **praktikum Pengolahan Citra Digital menggunakan Python dan OpenCV**.

Mahasiswa dapat menjalankan berbagai eksperimen seperti:

* Histogram Citra
* Histogram Equalization
* Brightness Adjustment
* Contrast Adjustment
* dan eksperimen pengolahan citra lainnya.

---

# 1. Persiapan Software

Pastikan sudah menginstall:

* Python 3.9 atau lebih baru
* Git (opsional jika menggunakan clone)

Cek versi Python:

```bash
python --version
```

---

# 2. Clone atau Download Project

### Menggunakan Git

```bash
git clone https://github.com/username/image-processing-lab.git
cd image-processing-lab
```

### Jika Download ZIP

1. Download repository dari GitHub
2. Extract file
3. Masuk ke folder project

```bash
cd image-processing-lab
```

---

# 3. Membuat Virtual Environment

Virtual environment digunakan agar dependency project terpisah dari Python global.

Buat virtual environment:

```bash
python -m venv venv
```

---

# 4. Mengaktifkan Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Mac / Linux

```bash
source venv/bin/activate
```

Jika berhasil, terminal akan menampilkan:

```
(venv)
```

---

# 5. Install Dependency

Install semua library yang dibutuhkan:

```bash
pip install -r requirements.txt
```

Library utama yang digunakan:

* opencv-python
* matplotlib
* numpy

---

# 6. Menjalankan Program

Project ini menggunakan **experiment runner** sehingga kita bisa menjalankan eksperimen tertentu.

Format perintah:

```bash
python main.py <nama_experiment>
```

Contoh menjalankan histogram citra:

```bash
python main.py histogram
```

---

# 7. Struktur Project

```
image-processing-lab
│
├── data
│   ├── input
│   │   └── image.png
│   └── output
│
├── src
│   ├── core
│   │   ├── loader.py
│   │   ├── display.py
│   │   └── path.py
│   │
│   ├── operations
│   │   └── histogram.py
│   │
│   └── experiments
│       └── exp_histogram.py
│
├── main.py
└── requirements.txt
```

Penjelasan:

| Folder          | Fungsi                     |
| --------------- | -------------------------- |
| data/input      | gambar untuk eksperimen    |
| data/output     | hasil eksperimen           |
| src/core        | fungsi dasar               |
| src/operations  | algoritma pengolahan citra |
| src/experiments | skenario eksperimen        |

---

# 8. Menambahkan Eksperimen Baru

1. Buat file baru di folder:

```
src/experiments
```

Contoh:

```
exp_blur.py
```

2. Tambahkan fungsi `run()`

```python
def run():
    print("Running blur experiment")
```

3. Tambahkan di `main.py`

```python
"blur": exp_blur.run
```

4. Jalankan:

```bash
python main.py blur
```

---

# 9. Dataset / Gambar

Masukkan gambar yang ingin diuji ke folder:

```
data/input
```

Contoh:

```
data/input/image.png
```

---

# 10. Troubleshooting

### ModuleNotFoundError

Pastikan menjalankan program dari folder project:

```
python main.py histogram
```

---

### Gambar tidak terbaca

Pastikan file gambar berada di:

```
data/input
```

---

# 11. Lisensi

Project ini digunakan untuk keperluan **pembelajaran Pengolahan Citra Digital**.
