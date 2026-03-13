from src.core.display import show_image
from src.core.loader import load_image
from src.core.path import image_path

# Mengimpor semua fungsi transformasi geometri yang telah dibuat
from src.operations.geometric_transform import (
    translate,
    rotate,
    scale,
    flip
)

def run():
    """
    Fungsi utama untuk mendemonstrasikan transformasi geometri:
    Pergeseran, Perputaran, Penskalaan, dan Pencerminan.
    """

    # 1. Persiapan Data
    path = image_path("image.png", "input")
    img = load_image(path)

    # 2. Eksekusi Transformasi Geometri

    # Geser gambar: 100 piksel ke kanan (x) dan 50 piksel ke bawah (y)
    translated = translate(img, 100, 50)

    # Putar gambar: -90 derajat (searah jarum jam) terhadap titik pusat
    rotated = rotate(img, -90)

    # Ubah skala: Lebar menjadi 0.5x (menyempit) dan Tinggi menjadi 1.5x (memanjang)
    # Ini akan menunjukkan efek distorsi aspek rasio
    scaled = scale(img, 0.5, 1.5)

    # Cermin gambar: mode -1 berarti dibalik secara horizontal DAN vertikal
    flipped = flip(img, -1)

    # 3. Visualisasi Hasil
    # Mahasiswa didorong untuk mengamati area kosong (biasanya hitam) 
    # yang muncul akibat pergeseran atau rotasi.
    show_image("Original", img)
    show_image("Translated (100, 50)", translated)
    show_image("Rotated (-90 deg)", rotated)
    show_image("Scaled (0.5w, 1.5h)", scaled)
    show_image("Flipped (Both Axes)", flipped)