from src.operations.histogram import show_histogram
from src.core.display import show_image
from src.core.loader import load_image
from src.core.path import image_path

# Mengimpor berbagai teknik transformasi histogram
from src.operations.histogram_transform import (
    change_brightness,
    change_contrast,
    histogram_equalization,
    histogram_specification
)

def run():
    # 1. Persiapan Data
    # Memuat gambar utama (source) yang akan dimodifikasi
    input_path = image_path("image.png")
    img = load_image(input_path, grayscale=True)

    # 2. Eksekusi Berbagai Transformasi Histogram
    
    # Menambah kecerahan (beta=60 membuat gambar lebih putih)
    brighter = change_brightness(img, 60)
    
    # Meningkatkan kontras (alpha=1.8 meregangkan distribusi intensitas)
    contrast = change_contrast(img, 1.8)
    
    # Perbaikan kontras otomatis menggunakan pemerataan histogram
    equalized = histogram_equalization(img)

    # 3. Histogram Specification (Matching)
    # Memerlukan gambar referensi untuk "ditiru" karakter pencahayaannya
    output_path = image_path("kontras-tinggi.png")
    ref = load_image(output_path, grayscale=True)
    specified = histogram_specification(img, ref)

    # 4. Menampilkan Hasil untuk Perbandingan
    # Bagian ini sangat krusial bagi mahasiswa untuk menganalisis hubungan 
    # antara perubahan Visual Gambar dengan bentuk Histogramnya.

    # Menampilkan Gambar Asli
    show_image("Original", img)
    show_histogram(img)

    # Menampilkan Hasil Perubahan Brightness
    # (Mahasiswa akan melihat grafik histogram bergeser ke kanan)
    show_image("Brightness", brighter)
    show_histogram(brighter)
    
    # Menampilkan Hasil Perubahan Kontras
    # (Mahasiswa akan melihat grafik histogram menjadi lebih lebar/renggang)
    show_image("Contrast", contrast)
    show_histogram(contrast)
    
    # Menampilkan Hasil Equalization
    # (Mahasiswa akan melihat grafik histogram menjadi lebih rata di seluruh intensitas)
    show_image("Equalization", equalized)
    show_histogram(equalized)
    
    # Menampilkan Hasil Specification
    # (Mahasiswa akan melihat histogram 'specified' memiliki bentuk yang mirip dengan histogram 'ref')
    show_image("Specification", specified)
    show_histogram(specified)