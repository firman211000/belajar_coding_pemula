from libs import wellcome_message, exit_program
from games import python    
from tools import warung

def menu():
    while True:
        print('Selamat datang di Permainan Tebak Python! \nPilih opsi: ')

        try:
            choose = int(input('\n1. Mulai Permainan \n2. Warung Pintar \n3. Keluar\n\nMasukkan pilihan Anda : '))
        except ValueError:
            print('Pilihan tidak valid. Silakan masukkan angka.')
            continue

        if choose == 1:
            return python.start()
        elif choose == 2:
            return warung.start()
        elif choose == 3:
            return
        else:
            print('Pilihan tidak valid. Silakan coba lagi.')

def main():
    wellcome_message()
    menu()
    exit_program()

if __name__ == "__main__":
    main()
