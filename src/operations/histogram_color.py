import cv2
import matplotlib.pyplot as plt

def show_histogram_color(image):
    # OpenCV membaca gambar dalam format BGR. 
    # Kita siapkan tuple warna untuk plotting dan label nama.
    colors = ('b', 'g', 'r')
    names = ('Blue', 'Green', 'Red')

    # -----------------------------
    # 1. Histogram masing-masing channel (Individu)
    # -----------------------------
    for i, col in enumerate(colors):
        # i adalah indeks (0, 1, 2) yang merujuk pada channel B, G, atau R
        # [i] menentukan channel mana yang dihitung histogramnya
        hist = cv2.calcHist([image], [i], None, [256], [0, 256])

        plt.figure(figsize=(6, 4))
        plt.plot(hist, color=col)
        plt.title(f"Histogram Channel: {names[i]}")
        plt.xlabel("Intensity (0-255)")
        plt.ylabel("Number of Pixels")
        plt.xlim([0, 256])
        plt.show()

    # -----------------------------
    # 2. Histogram gabungan RGB (Overlay)
    # -----------------------------
    plt.figure(figsize=(10, 6))
    
    for i, col in enumerate(colors):
        hist = cv2.calcHist([image], [i], None, [256], [0, 256])
        # Kita menggambar ketiga garis dalam satu plt.figure yang sama
        plt.plot(hist, color=col, label=names[i], linewidth=1.5)

    plt.title("Histogram RGB (Combined Representation)")
    plt.xlabel("Intensity Value")
    plt.ylabel("Frequency")
    plt.legend() # Menampilkan keterangan warna (Blue, Green, Red)
    plt.xlim([0, 256])
    plt.grid(alpha=0.3)
    plt.show()