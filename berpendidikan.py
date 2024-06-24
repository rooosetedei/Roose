
def pintar():
    import mainmodul
    
    print('\nHALO , SELAMAT DATANG')

    while True:
        import os
        def luasbola():
            jari = float(input("masukan jari-jari bola: "))
            hasil = 4 * 3.14 *  jari * jari
            rumus = f"4 * 3.14 * {jari} * {jari} = "
            print(rumus)
            return hasil


        def luaskerucut():
            jari2 = float(input("masukan jari jari kerucut: "))
            garpel = float(input("masukan garis pelukis kerucut: "))
            rumus = f"3.14 x {jari2} x ({jari2} + {jari2}) = "
            hasil = 3.14 * jari2 * (jari2 + garpel )
            print(rumus)
            return hasil

        def luasprismasegitigasikusiku():
            als = float(input("masukan sisi alas segitiga: "))
            tg = float(input("masukan sisi tinggi segitiga: "))
            mr = float(input("masukan sisi miring segitiga: "))
            tgp = float(input("masukan tinggi prisma: "))
            rumus = f"2 x ( 1/2 x {als} x {tg} + ({als} + {mr} + {tgp})) ="
            hasil = 2 * ( 0.5 *  als * tg) + (als + tg + mr * tgp)
            print(rumus)
            return hasil
            
            
        def luastabung():
            r = float(input("masukan jari-jari tabung: "))
            tn = float(input("masukan tinggi tabung: "))
            rumus= f"3,14 x {r} x {r} x {tn}"
            hasil = 3.14 * r * r * tn
            print(rumus)
            return hasil

        def luasjajargenjang():
            al = float(input("masukan alas jajar genjang: "))
            tt = float(input("masukan tinggi jajar genjang: "))
            rumus = f"{al} x {tt} = "
            hasil = al * tt
            print(rumus)
            return hasil
        
        pilihanuser = int(input('''\n1.luas bola\n2.luas kerucut\n3.luas prisma segitiga siku-siku\n4.luas tabung\n5.luas jajargenjang
        rumus nomor berapa yang ingin kamu gunakan:'''))
        os.system('cls')#<<untuk melakukan clear semua command ketika mekeksekusi function (import terlebih dahulu)
        if pilihanuser == 1:
                print(luasbola())
        elif pilihanuser == 2:
                print(luaskerucut())
        elif pilihanuser == 3:
                print(luasprismasegitigasikusiku())
        elif pilihanuser == 4:
                print(luastabung())
        elif pilihanuser == 5:
                print(luasjajargenjang())
        else:
                print("tolong pilih nomor yang ada: ")
        playagain = input("ingin melanjutkan program? ya/tidak: ")
        if playagain == 'tidak':
            
            mainmodul.daftar()
            
            


            
