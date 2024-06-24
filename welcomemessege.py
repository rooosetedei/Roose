from time import sleep
def sambutan_lol(sambutan):
    
    
    style = "=" * (len(sambutan) + 6)#<<<< jika ada variabel di dalam kurung function artinya harus di isi ketika 
                                     #akan di output.
    print(style)
    print(f"==={sambutan}===")
    print(style)
    
def times():
    print("program akan dihentikan dalam ")
    sleep(1)
    print('3..')
    sleep(1)
    print('2..')
    sleep(1)
    print('1..')
    sleep(1)
    print('program dihentikan')
    exit()
if __name__ == '__main__':
    times()
    sambutan_lol()

    
    
    

