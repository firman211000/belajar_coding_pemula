import socket
PC_NAME = socket.gethostname()
from time import sleep

def wellcome_message():

    style = "*" * (len(PC_NAME) + 6)
    print(style)
    print(f"** {PC_NAME} **")
    print(style)

def exit_program():
    print("Program akan keluar dalam 3 detik...")
    sleep(1)
    print("3....")
    sleep(1)
    print("2....")
    sleep(1)
    print("1....")
    print("Program keluar. Terima kasih sudah bermain!")

if __name__ == "__main__":
    wellcome_message()
    exit_program()
