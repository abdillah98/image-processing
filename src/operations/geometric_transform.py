import cv2
import numpy as np


# --------------------------------
# 1. Translasi
# --------------------------------
def translate(image, tx, ty):

    # Mengambil dimensi citra (tinggi dan lebar)
    # image.shape[:2] mengambil 2 nilai pertama (h, w) dari tuple shape
    h, w = image.shape[:2]

    # Mendefinisikan Matriks Transformasi M (2x3)
    # [1, 0, tx] -> 1: skala x tetap, 0: tidak ada kemiringan, tx: jarak geser x
    # [0, 1, ty] -> 0: tidak ada kemiringan, 1: skala y tetap, ty: jarak geser y
    M = np.float32([
        [1, 0, tx],
        [0, 1, ty]
    ])

    # Fungsi warpAffine menerapkan matriks M ke setiap piksel
    # (w, h) di akhir menentukan ukuran kanvas output (lebar, tinggi)
    translated = cv2.warpAffine(image, M, (w, h))

    return translated


# --------------------------------
# 2. Rotasi
# --------------------------------
def rotate(image, angle, scale=1.0):

    # Mengambil dimensi citra
    h, w = image.shape[:2]

    # Menentukan titik poros rotasi (Center)
    # Menggunakan pembagian bulat (//) agar koordinat berupa integer
    # (w//2, h//2) berarti titik pusat berada tepat di tengah gambar
    center = (w // 2, h // 2)

    # Membuat Matriks Rotasi M menggunakan fungsi bawaan OpenCV
    # Parameter: (titik_pusat, sudut_derajat, skala_gambar)
    # Angle positif = berlawanan arah jarum jam
    M = cv2.getRotationMatrix2D(center, angle, 1.0)

    # Menerapkan rotasi ke citra berdasarkan matriks M yang dihasilkan
    # Menggunakan interpolasi bicubic agar hasil rotasi lebih halus (tidak pecah)
    rotated = cv2.warpAffine(image, M, (w, h), flags=cv2.INTER_CUBIC)

    return rotated


# --------------------------------
# 3. Scaling
# --------------------------------
def scale(image, fx, fy):

    # cv2.resize adalah fungsi utama untuk mengubah dimensi citra.
    scaled = cv2.resize(
        image,      # Citra sumber yang akan diubah ukurannya.
        None,       # dsize (ukuran output) diisi None karena kita menggunakan faktor skala (fx, fy).
        fx=fx,      # Faktor skala horizontal (misal: 2.0 artinya lebar jadi 2x lipat).
        fy=fy,      # Faktor skala vertikal (misal: 0.5 artinya tinggi jadi setengahnya).
        
        # Interpolasi menentukan bagaimana OpenCV mengisi/menghitung piksel baru.
        # INTER_LINEAR (Bilinear) adalah standar yang seimbang antara kecepatan dan kualitas.
        interpolation=cv2.INTER_LINEAR 
    )

    return scaled


# --------------------------------
# 4. Flipping
# --------------------------------
def flip(image, mode):
    """
    Fungsi untuk melakukan pencerminan (mirroring) pada citra.
    
    Parameter mode:
    0  -> Vertical Flip: Membalik gambar secara vertikal (atas ke bawah).
    1  -> Horizontal Flip: Membalik gambar secara horizontal (kiri ke kanan).
    -1 -> Both Axes: Membalik gambar pada kedua sumbu (seperti diputar 180 derajat).
    """

    # cv2.flip adalah fungsi efisien untuk menukar posisi piksel berdasarkan sumbu.
    # Secara matematis, ini mengubah indeks array tanpa perlu matriks transformasi kompleks.
    flipped = cv2.flip(image, mode)

    return flipped