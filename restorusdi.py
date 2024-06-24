from services import db
# from welcomemessege import times
import mainmodul 


def update():
    kode = input('masukan kode untuk hidangan :')
    nama =input('masukan nama untuk hidangan : ')
    stok =int(input('masukan stok hidangan : '))
    harga= int(input('masukan harga hidangan : '))
    db.masukanitem(kode, nama, stok , harga)
    
    
def review():
    item = db.show_ITEM()
    for items in item:
      kode_hidangan = items[1]
      nama_hidangan = items[2]
      stok_hidangan = items[3]
      harga_hidangan = items[4]
      print(f''' 
KODE HIDANGAN = {kode_hidangan}
NAMA MAKANAN = {nama_hidangan}
STOK MAKANANAN = {stok_hidangan}
HARGA MAKANAN =  {harga_hidangan}\n''')
    
    
def bukaresto():
    while True:
        userrinput = int(input('menu pilihan \n1.Masukan menu hidangan baru \n2.Cek menu hidangan \n3.Kembali \nTentukan pilihan anda :'))
        if userrinput == 1:
            update()
        elif userrinput == 2:
            review()
        elif userrinput == 3:
            mainmodul.daftar()
        else:
            print('pilih sesuai pilihan')
            break

# if __name__ == '__main__':
#     bukaresto()
    
        
        
    

        