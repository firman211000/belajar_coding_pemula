import main
from services import db

def add():
    kode_barang = input("Masukkan kode barang: ")
    nama_barang = input("Masukkan nama barang: ")
    harga_barang = input("Masukkan harga barang: ")
    stok_barang = input("Masukkan stok barang: ")

    db.insert_item(kode_barang, nama_barang, harga_barang, stok_barang)
    
def check():
    items = db.fetch_items()

    if not items:
        print("\nBelum ada data barang.")
        return

    headers = ("No", "Kode Barang", "Nama Barang", "Harga", "Stok")
    rows = []

    for item in items:
        rows.append((
            str(item[0]),
            str(item[1]),
            str(item[2]),
            str(item[3]),
            str(item[4]),
        ))

    widths = [len(header) for header in headers]

    for row in rows:
        for index, value in enumerate(row):
            widths[index] = max(widths[index], len(value))

    separator = "+-" + "-+-".join("-" * width for width in widths) + "-+"
    header = "| " + " | ".join(
        title.ljust(widths[index]) for index, title in enumerate(headers)
    ) + " |"

    print("\nDaftar Barang:")
    print(separator)
    print(header)
    print(separator)

    for row in rows:
        formatted_row = []

        for index, value in enumerate(row):
            if index in (0, 3, 4):
                formatted_row.append(value.rjust(widths[index]))
            else:
                formatted_row.append(value.ljust(widths[index]))

        print("| " + " | ".join(formatted_row) + " |")

    print(separator)

def start():
    #Menampilkan halaman warung sampai pengguna kembali ke menu.
    while True:
        
        menu = int(input("\nSelamat datang di Warung Pintar! \nPilih opsi:\n\n1. Tambah barang\n2. Lihat barang\n3. Kembali ke menu utama\n\nMasukkan pilihan Anda: "))

        if menu == 1:
            add()
        elif menu == 2:
            check()
        elif menu == 3:
            main.menu()
        else:
            break
        
if __name__ == "__main__":
    start()
