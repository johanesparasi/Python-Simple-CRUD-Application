checkBol = False

while checkBol == False:
    print('========================= MENU TRANSAKSI =========================')
    print('Silahkan pilih Kategori')
    print('1. Rumah Tangga')
    print('2. Elektronik')
    print('3. Logout')
    pilihMenu = input('Silahkan masukkan pilihan: ')

    if pilihMenu == '1':
        exec(open('rumahTangga.py').read())
        checkBol = True
    elif pilihMenu == '2':
        exec(open('elektronik.py').read())
        checkBol = True
    elif pilihMenu == '3':
        exec(open('main.py').read())
        checkBol = True
    else:
        print('Masukkan pilihan yang benar!')
        checkBol = False


