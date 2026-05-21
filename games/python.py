import random
import latihan1

def start():
    while True:
        bentuk_python = "🐤"
        start_index = 1
        kotak = random.randint(1, 4)

        python_kosong = [bentuk_python] * 4
        python = python_kosong.copy()
        python[kotak - start_index] = "🐍"

        python_kosong = " ".join(python_kosong)
        python = " ".join(python)

        print(f'\nCoba perhatikan bebek di bawah ini. \nAda 4 kotak yang berisi bebek, tetapi hanya satu kotak yang berisi python asli. \nCoba tebak di mana letak python tersebut!\n{python_kosong}\n')

        pilihan_user = int(input("Masukkan nomor kotak yang kamu pilih (1-4): "))

        if kotak == pilihan_user:
            print(f"\nSelamat kamu benar, python berada di kotak nomor {kotak}. \n{python}")
        else:
            print(f"\nMaaf kamu salah, python berada di kotak nomor {kotak}.\n{python}")

        while True:
            play_again = input("\nApakah kamu ingin bermain lagi? (y/n): ").strip().lower()

            if play_again == "y":
                break

            if play_again == "n":
                return latihan1.menu()

            print("Input tidak valid. Harap masukkan 'y' atau 'n'.")

if __name__ == "__main__":
    start()
