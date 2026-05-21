from helpers import input_ya_tidak


def start():
    """Menampilkan halaman warung sampai pengguna kembali ke menu."""
    while True:
        print("\nIni warung apps!")
        kembali_ke_menu = input_ya_tidak("Kembali ke menu utama? (y/n): ")

        if kembali_ke_menu == "y":
            # Return menghentikan warung dan membawa program kembali ke menu.
            return

        print("Kamu masih berada di warung.")


if __name__ == "__main__":
    start()
