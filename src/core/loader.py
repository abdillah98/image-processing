import cv2

def load_image(path, grayscale=False):
    """
    Fungsi untuk membaca file gambar dari media penyimpanan.
    """
    if grayscale:
        # Membaca gambar langsung dalam mode hitam-putih (1 channel)
        img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    else:
        # Membaca gambar dalam mode warna asli (BGR - 3 channel)
        img = cv2.imread(path)

    # Validasi: Cek apakah gambar berhasil dimuat atau tidak (misal: path salah)
    if img is None:
        # Jika file tidak ditemukan, program akan berhenti dan memberikan pesan error yang jelas
        raise Exception(f"Gambar tidak ditemukan pada lokasi: {path}")

    return img