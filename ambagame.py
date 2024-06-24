 
def ambagame():
  
  import mainmodul
  from welcomemessege import times
  import os
  import random
  from welcomemessege import sambutan_lol



  sambutan_lol("SELAMAT DATANG DI AMBA GAME")

  nama_user = input("masukan nama kalian: ")
  #<<<<<<di deklarasikan

  # print(jumlahgoa)
  # print(f"posisi ambatukam : {Ambatukam_position}")



  while nama_user == "":
    nama_user = input("Tolong isi Nama anda wak : ")
    
  while True:
    Ambatukam_position = random.randint(1,4)
    goa_ambatukam = "[_]"
    jumlahgoa = [goa_ambatukam] * 4
    goa_bolong = jumlahgoa.copy()
    jumlahgoa[Ambatukam_position-1] = "[0_0]"
    goa_bolong = ' '.join(goa_bolong)
    anjay = ' '.join(jumlahgoa)
      
    print(f'''
          
          
          halo {nama_user} !
          
    perhatikan 4 lubang ini!
                            
                            {goa_bolong}
                             1   2   3   4
                            
                            
    kamu punya 1 kesempatan saja untuk mengubah jawaban jika tidak yakin ''')
                                                                      

    pilihan_user =  int(input('''menurut kamu di lubang berapa ambatukam bersembunyi?
                        
                        [ 1  
                          2 
                          3 
                          4]         jawab:'''))

    while pilihan_user > 4:
      
      
      pilihan_user = int(input ("tolong isi sesuai pilihan yang sudah ditentukan : "))
      
    
    validasi = input(f"apakah kamu yakin ambatukam berada di lubang {pilihan_user} [ya/tidak] :")
    os.system('cls')

    if validasi == "ya":
      if pilihan_user == Ambatukam_position:
        print(F"{anjay} \n SELAMAT KAMU BENAR ambatukam berada di lubang {Ambatukam_position } 🏆")
      else:
        print(F"{anjay} \n MAAF KAMU SALAH ambatukam tidak berada di lubang {pilihan_user} tapi dia di lubang {Ambatukam_position } 🙊 ")
    elif validasi == "tidak":
      pilihan_user =  int(input('''menurut kamu dimana ambatukam bersembunyi?
                        
                        [ 1  
                          2 
                          3 
                          4]         jawab:'''))
      
      
      p = 1
      o = 2
      k = 3
      j = 4
      
      while pilihan_user != p and o and k and j: 
          pilihan_user = int(input ("tolong isi sesuai pilihan yang sudah ditentukan : "))
    
      
      if pilihan_user == Ambatukam_position:
        print(F" {anjay} \n KAMU BENAR AMBATUKAM BERADA DI LUBANG NOMOR {Ambatukam_position}")
      else:
        print(F" {anjay} \n KAMU SALAH AMBATUKAM TIDAK BERADA DI LUBANG {pilihan_user} TAPI DIA BERADA DI LUBANG {Ambatukam_position}")
        
    else:
      print("JAWAB YANG BENER DONG!!!!!")
      exit()
    
    
    mainlagi = input("mau main lagi wak? [ya/tidak] : ")
    
    if mainlagi == "tidak":

      
     
     mainmodul.daftar()
    else:
      print("JAWABAN TIDAK VALID")
      times()
      
      
    

     
  
  


    
      
  
      
    
          
    



    
    
    
    
        
      
  
    
    
    
  

      
          



        
      