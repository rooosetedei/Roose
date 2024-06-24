import mysql.connector 

db = mysql.connector.connect(
    host ='localhost',
    user ='root',
    password ='',
    database ='restorusdi'
    
)

def masukanitem(kode_hidangan, nama_hidangan, stok_hidangan, harga_hidangan):
    cursor = db.cursor()
    cursor.execute("INSERT INTO inv_hidangan (kode_hidangan, nama_hidangan, stok_hidangan, harga_hidangan) VALUES (%s, %s, %s, %s)",
                   (kode_hidangan, nama_hidangan, stok_hidangan, harga_hidangan))
    db.commit() 
    if cursor.rowcount > 0 :
        print('data berhasil di masukan')
    else:
        print('data gagal di masukan')    
    
def show_ITEM():
    cursor = db.cursor()
    cursor.execute('SELECT * FROM inv_hidangan')
    
    return cursor.fetchall()
__name__ = 'lolo'
print(__name__.__dict__)