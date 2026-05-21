import latihan1


def start():
    while True:
        print("ini warung apps!")
        play_again = input("kembali ke menu utama? [y/n] \n")

        if play_again == "y":
            return latihan1.menu()

if  __name__ == "__main__":
    start()
