"""File penghubung untuk helper dengan nama lama.

Fungsi bantuan utama sekarang berada di helpers.py.
"""

from helpers import keluar_program, tampilkan_judul


def welcome_message():
    tampilkan_judul("Program Belajar Python")


def wellcome_message():
    welcome_message()


def exit_program():
    keluar_program()


if __name__ == "__main__":
    welcome_message()
    exit_program()
