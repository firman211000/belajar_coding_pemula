import socket 
from time import sleep

hostname = socket.gethostname()

def tampilkan_judul():
    #Menampilkan judul program dengan hiasan garis bintang.
    garis = "*" * (len(hostname) + 6)

    print(garis)
    print(f"** {hostname} **")
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
    tampilkan_judul()
    keluar_program()
