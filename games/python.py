"""File penghubung untuk nama lama game.

Game tebak python sekarang berada di tebak_python.py.
"""

if __package__:
    from .tebak_python import start
else:
    from tebak_python import start


if __name__ == "__main__":
    start()
