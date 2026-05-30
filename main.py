from games import tebak_python
from helpers import keluar_program, tampilkan_judul
from tools import warung


def menu():
    #Menampilkan menu utama sampai pengguna memilih keluar.
    while True:
        print("\nSelamat datang di program belajar Python!")
        print("Pilih menu:")
        print("1. Mulai permainan tebak python")
        print("2. Buka warung pintar")
        print("3. Keluar")

        pilihan = input("Masukkan pilihan Anda: ")  #Pilihan pengguna tidak boleh string
        if not pilihan.isdigit():       
            print("Pilihan tidak valid. Silakan masukkan angka.")
            continue

        pilihan_menu = int(pilihan) #Konversi string ke integer untuk validasi pilihan menu
        if pilihan_menu < 1 or pilihan_menu > 3:
            print("Pilihan tidak tersedia. Silakan pilih 1, 2, atau 3.")
            continue

        if pilihan_menu == 1:
            tebak_python.start()
        elif pilihan_menu == 2:
            warung.start()
        else:
            break
def main():
    #Menjalankan program dari awal sampai selesai
    tampilkan_judul()
    menu()
    keluar_program()


# Kode di bawah ini berjalan saat file main.py dibuka langsung.
if __name__ == "__main__":
    main()
