import sys
# Mengimpor seluruh skenario praktikum dari folder experiments
from src.experiments import ( 
    exp_histogram, 
    exp_histogram_transform, 
    exp_histogram_color,
    exp_geometric_transform
)

# Menggunakan Dictionary untuk memetakan nama perintah ke fungsi 'run' masing-masing modul
# Ini memudahkan penambahan eksperimen baru tanpa banyak 'if-else'
experiments = {
    "histogram": exp_histogram.run,
    "histogram_color": exp_histogram_color.run,
    "transform_histogram": exp_histogram_transform.run,
    "geometri": exp_geometric_transform.run
}

if __name__ == "__main__":
    # Mengecek apakah user memberikan argumen saat menjalankan program
    # Contoh penggunaan: python main.py geometri
    if len(sys.argv) < 2:
        print("Gunakan format: python main.py [nama_eksperimen]")
        print("Daftar eksperimen yang tersedia:")
        for k in experiments:
            print("-", k)
        exit()

    # Mengambil nama eksperimen dari argumen terminal pertama
    exp_name = sys.argv[1]

    # Menjalankan fungsi run() sesuai dengan input dari user
    if exp_name in experiments:
        print(f"Menjalankan eksperimen: {exp_name}...")
        experiments[exp_name]()
    else:
        print(f"Eksperimen '{exp_name}' tidak ditemukan.")
        print("Pastikan penulisan sudah benar sesuai daftar di atas.")