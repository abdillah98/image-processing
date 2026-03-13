import cv2

def show_image(title, img):
    """
    Fungsi untuk menampilkan citra dalam sebuah jendela (window).
    """
    # Menampilkan gambar pada jendela dengan judul tertentu
    cv2.imshow(title, img)
    
    # waitKey(0) menahan jendela agar tetap terbuka sampai pengguna menekan tombol apapun di keyboard.
    # Tanpa ini, jendela akan muncul dan langsung tertutup dalam sekejap.
    cv2.waitKey(0)
    
    # Menutup semua jendela OpenCV yang sedang terbuka setelah tombol ditekan.
    cv2.destroyAllWindows()