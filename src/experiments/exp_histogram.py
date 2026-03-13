# Mengimpor modul-modul pendukung yang telah dibuat sebelumnya
# Konsep ini mengajarkan mahasiswa untuk menjaga kode tetap rapi dan terorganisir
from src.core.display import show_image
from src.core.path import image_path
from src.core.loader import load_image
from src.operations.histogram import show_histogram

def run():
    """
    Fungsi utama untuk menjalankan alur praktikum: 
    Cari gambar -> Muat gambar -> Tampilkan gambar -> Analisis Histogram.
    """
    
    # 1. Menentukan lokasi file secara dinamis
    # Memanggil file "kontras-tinggi.png" yang berada di folder data/input/
    path = image_path("kontras-tinggi.png")
    
    # 2. Membaca gambar ke dalam memori
    # Kita gunakan grayscale=True karena analisis histogram dasar lebih mudah dipahami dalam hitam-putih
    img = load_image(path, grayscale=True)

    # 3. Visualisasi Hasil
    # Menampilkan gambar asli dalam jendela pop-up
    show_image("Citra Asli (Grayscale)", img)
    
    # 4. Analisis Data
    # Menampilkan grafik distribusi (histogram) intensitas piksel untuk melihat karakter kontras gambar
    show_histogram(img)