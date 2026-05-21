import random


JUMLAH_KOTAK = 4
IKON_BEBEK = "🐤"
IKON_PYTHON = "🐍"


def input_main_lagi():
    """Meminta jawaban y atau n setelah satu ronde selesai."""
    while True:
        jawaban = input("\nApakah kamu ingin bermain lagi? (y/n): ").strip().lower()

        if jawaban == "y" or jawaban == "n":
            return jawaban

        print("Input tidak valid. Harap masukkan 'y' atau 'n'.")


def start():
    """Menjalankan game tebak python sampai pemain memilih berhenti."""
    while True:
        # Posisi python diacak ulang setiap ronde.
        posisi_python = random.randint(1, JUMLAH_KOTAK)

        # Kotak tertutup hanya menampilkan bebek kepada pemain.
        kotak_tertutup = [IKON_BEBEK] * JUMLAH_KOTAK

        # Kotak jawaban memperlihatkan posisi python yang sebenarnya.
        kotak_jawaban = kotak_tertutup.copy()
        kotak_jawaban[posisi_python - 1] = IKON_PYTHON

        tampilan_kotak = " ".join(kotak_tertutup)
        tampilan_jawaban = " ".join(kotak_jawaban)

        print("\nCoba perhatikan bebek di bawah ini.")
        print("Ada 4 kotak, tetapi hanya satu yang berisi python asli.")
        print("Coba tebak di mana letak python tersebut!")
        print(f"\n{tampilan_kotak}\n")

        while True:
            input_pilihan = input("Masukkan nomor kotak yang kamu pilih (1-4): ").strip()

            if not input_pilihan.isdigit():
                print("Input tidak valid. Harap masukkan angka.")
                continue

            pilihan_user = int(input_pilihan)

            if pilihan_user < 1 or pilihan_user > JUMLAH_KOTAK:
                print("Pilihan tidak valid. Pilih nomor 1 sampai 4.")
                continue

            break

        if pilihan_user == posisi_python:
            print(f"\nSelamat, tebakan kamu benar! Python ada di kotak nomor {posisi_python}.")
        else:
            print(f"\nMaaf, tebakan kamu salah. Python ada di kotak nomor {posisi_python}.")

        print(tampilan_jawaban)

        main_lagi = input_main_lagi()

        if main_lagi == "n":
            # Return menghentikan game dan membawa program kembali ke menu.
            return


if __name__ == "__main__":
    start()
