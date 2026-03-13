import cv2
import matplotlib.pyplot as plt

def show_histogram(image):
    # cv2.calcHist(images, channels, mask, histSize, ranges)
    # 1. [image]: Citra input (harus dalam list []).
    # 2. [0]: Indeks channel. Untuk grayscale hanya ada satu channel, yaitu 0.
    # 3. None: Mask (opsional). Jika None, berarti menghitung seluruh bagian gambar.
    # 4. [256]: Bin count. Jumlah "kotak" distribusi (0-255).
    # 5. [0, 256]: Range nilai intensitas yang dihitung (0 sampai 255).
    hist = cv2.calcHist([image], [0], None, [256], [0, 256])

    # Visualisasi menggunakan Matplotlib
    plt.figure(figsize=(8, 5)) # Mengatur ukuran jendela plot
    plt.plot(hist, color='black') # Menampilkan garis histogram
    plt.title("Histogram Intensitas Grayscale")
    plt.xlabel("Tingkat Keabuan (0-255)")
    plt.ylabel("Jumlah Piksel")
    
    # Menambahkan grid agar lebih mudah dibaca
    plt.grid(axis='y', alpha=0.75)
    
    # Membatasi sumbu X agar pas di angka 0-255
    plt.xlim([0, 256])
    
    plt.show()