from time import sleep


def tampilkan_judul(judul):
    """Menampilkan judul program dengan hiasan garis bintang."""
    garis = "*" * (len(judul) + 6)

    print(garis)
    print(f"** {judul} **")
    print(garis)


def keluar_program():
    """Menampilkan hitung mundur sederhana sebelum program selesai."""
    print("Program akan keluar dalam 3 detik...")

    sleep(1)
    print("3....")

    sleep(1)
    print("2....")

    sleep(1)
    print("1....")

    print("Program keluar. Terima kasih sudah bermain!")


if __name__ == "__main__":
    tampilkan_judul("Program Belajar Python")
    keluar_program()
