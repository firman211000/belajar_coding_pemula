def start():
    #Menampilkan halaman warung sampai pengguna kembali ke menu.
    while True:
        print("\nIni warung apps!")

        while True:
            kembali_ke_menu = input("Kembali ke menu utama? (y/n): ").strip().lower()

            if kembali_ke_menu == "y":
                # Return menghentikan warung dan membawa program kembali ke menu.
                return

            if kembali_ke_menu == "n":
                print("Kamu masih berada di warung.")
                break

            print("Input tidak valid. Harap masukkan 'y' atau 'n'.")


if __name__ == "__main__":
    start()
