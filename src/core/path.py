import os

def image_path(image_name, type="input"):
    """
    Fungsi untuk menyusun lokasi file (path) secara dinamis.
    Membantu mengelola struktur folder proyek agar rapi.
    """
    # Mengambil lokasi folder tempat script ini berada
    base_path = os.path.dirname(__file__)
    
    # Mencari root project (naik 2 level folder: ../..)
    # Gunakan ini agar script bisa menemukan folder 'data' meskipun script dijalankan dari sub-folder
    project_root = os.path.abspath(os.path.join(base_path, "..", ".."))
    
    # Menyusun path lengkap ke file gambar: project_root/data/[input/output]/nama_gambar
    input_path = os.path.join(project_root, "data", type, image_name)
    
    return input_path