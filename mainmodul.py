import os
import welcomemessege 
import ambagame
import restorusdi
import berpendidikan
from welcomemessege import times
import restorusdi

if __name__ == "__main__":
  welcomemessege.sambutan_lol("     SELAMAT DATANG      ")

def daftar():
    option2 = int(input("\ndaftar program \n1.Amba game😎 \n2.restoran mas rusdi🧑‍🍳  \n3.berpendidikan🤓 \n4.keluar program🏃‍♂️ \nprogram nomor berapa yang ingin anda jalankan : "))
    while option2 > 4:
     option2 = int(input("pilih nomor sesuai yang ada di daftar: "))
    return option2

def programoption():
    while True:
        option = daftar()
        os.system('cls')
        if option == 4:
            times()
            print("SILAHKAN DATANG KEMBALI")
        elif option == 1:
            ambagame.ambagame()
        elif option == 2:
            restorusdi.bukaresto()
            # os.system('cls')   
        elif option == 3:
            berpendidikan.pintar()
        elif option(str):
            print("p2erintah tidak valid")   
            times()



if __name__ == '__main__':
    programoption()
    welcomemessege.sambutan_lol()
    daftar()



        
        

        
    