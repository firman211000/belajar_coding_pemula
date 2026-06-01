import mysql.connector

db = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='warung_mini'
        )

def insert_item(kode_barang, nama_barang, harga_barang, stok_barang):
    cursor = db.cursor()
    cursor.execute("INSERT INTO tbl (kode_barang, nama_barang, harga_barang, stok_barang) VALUES (%s, %s, %s, %s)", (kode_barang, nama_barang, harga_barang, stok_barang))
    db.commit()
    if cursor.rowcount > 0:
        print("Data berhasil disimpan.")
    else:
        print("Gagal menyimpan data.")

def fetch_items():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM tbl")
    return cursor.fetchall()
    