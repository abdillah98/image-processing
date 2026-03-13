import cv2
import numpy as np

# -----------------------------
# 1. Pengubahan Kecerahan (Brightness)
# -----------------------------
def change_brightness(image, beta=50):
    """
    Operasi penjumlahan/pengurangan konstanta pada setiap piksel.
    Rumus: g(x,y) = f(x,y) + beta
    """
    # cv2.convertScaleAbs memastikan nilai tetap di rentang 0-255 (saturasi)
    result = cv2.convertScaleAbs(image, alpha=1, beta=beta)
    return result

# -----------------------------
# 2. Pengubahan Kontras
# -----------------------------
def change_contrast(image, alpha=1.5):
    """
    Operasi perkalian piksel dengan konstanta (gain).
    Rumus: g(x,y) = alpha * f(x,y)
    alpha > 1: Merenggangkan histogram (kontras tinggi)
    alpha < 1: Menyempitkan histogram (kontras rendah)
    """
    result = cv2.convertScaleAbs(image, alpha=alpha, beta=0)
    return result

# -----------------------------
# 3. Histogram Equalization
# -----------------------------
def histogram_equalization(image):
    """
    Meningkatkan kontras secara otomatis dengan meratakan distribusi intensitas.
    Sangat efektif untuk citra yang terlalu gelap atau terlalu terang secara keseluruhan.
    Catatan: Hanya untuk citra grayscale.
    """
    result = cv2.equalizeHist(image)
    return result

# -----------------------------
# 4. Histogram Specification (Matching)
# -----------------------------
def histogram_specification(source, reference):
    """
    Memaksa citra 'source' memiliki gaya pencahayaan yang sama dengan 'reference'.
    Menggunakan teknik CDF (Cumulative Distribution Function) mapping.
    """
    # Menghitung histogram dan CDF untuk kedua citra
    src_hist, bins = np.histogram(source.flatten(), 256, [0,256])
    ref_hist, bins = np.histogram(reference.flatten(), 256, [0,256])

    # cdf.cumsum() mengakumulasi jumlah piksel dari intensitas 0 hingga 255
    src_cdf = src_hist.cumsum()
    ref_cdf = ref_hist.cumsum()

    # Normalisasi CDF agar rentangnya 0.0 - 1.0
    src_cdf_normalized = src_cdf / src_cdf.max()
    ref_cdf_normalized = ref_cdf / ref_cdf.max()

    # Membuat tabel pemetaan (Lookup Table)
    mapping = np.zeros(256, dtype=np.uint8)
    for i in range(256):
        # Mencari nilai intensitas di reference yang CDF-nya paling mirip dengan source
        diff = np.abs(ref_cdf_normalized - src_cdf_normalized[i])
        mapping[i] = np.argmin(diff)

    # Menerapkan tabel pemetaan ke citra asli
    result = mapping[source]
    return result