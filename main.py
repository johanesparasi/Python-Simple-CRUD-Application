checkBol = False

while checkBol == False:
    print('========================= Selamat Datang di PSP MART =========================')
    print('Silahkan pilih menu')
    print('1. Login')
    print('2. Register')
    pilihMenu = input('Silahkan masukkan pilihan: ')

    def mainMenu():
        exec(open('login.py').read())

    def registerMenu():
        exec(open('register.py').read())

    if pilihMenu == '1':
        mainMenu()
        checkBol = True
    elif pilihMenu == '2':
        registerMenu()
        checkBol = True
    else:
        print('Masukkan pilihan yang benar!')
        checkBol = False


