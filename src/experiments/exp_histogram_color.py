# Mengimpor fungsi khusus untuk analisis warna dan fungsi dasar lainnya
from src.operations.histogram_color import show_histogram_color
from src.core.display import show_image
from src.core.path import image_path
from src.core.loader import load_image
from src.operations.histogram import show_histogram

def run():
    """
    Fungsi utama untuk mendemonstrasikan analisis histogram pada citra berwarna.
    Mahasiswa akan melihat bagaimana distribusi warna tersebar di channel Blue, Green, dan Red.
    """
    
    # 1. Mengambil path gambar
    path = image_path("image.png")
    
    # 2. Memuat gambar dalam mode warna (BGR)
    # Sangat penting: grayscale=False memastikan kita mendapatkan 3 channel warna.
    # Jika diatur True, fungsi show_histogram_color akan error atau memberikan hasil salah.
    img = load_image(path, grayscale=False)

    # 3. Menampilkan citra asli agar mahasiswa bisa membandingkan warna visual 
    # dengan data statistik di histogram.
    show_image("Citra Berwarna (Original)", img)
    
    # 4. Melakukan analisis histogram warna
    # Fungsi ini akan membedah citra menjadi 3 komponen warna dasar.
    show_histogram_color(img)