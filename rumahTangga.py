import buy

checkBol = False

print('========================= RUMAH TANGGA =========================')
print('Silahkan pilih Barang')
print('1. Kursi')
print('2. Kompor')
print('3. Meja')
print('4. Lemari')
print('5. Kembali')

while checkBol == False:
    try:
        pilihMenu = int(input('Silahkan Masukkan Pilihan: '))
        if pilihMenu == 1:
            inputQty = int(input('Silahkan Masukkan Jumlah Barang: '))
            buy.buyFunction('KURSI', inputQty)
            checkBol = True
        elif pilihMenu == 2:
            inputQty = int(input('Silahkan Masukkan Jumlah Barang: '))
            buy.buyFunction('KOMPOR', inputQty)
            checkBol = True
        elif pilihMenu == 3:
            inputQty = int(input('Silahkan Masukkan Jumlah Barang: '))
            buy.buyFunction('MEJA', inputQty)
            checkBol = True
        elif pilihMenu == 4:
            inputQty = int(input('Silahkan Masukkan Jumlah Barang: '))
            buy.buyFunction('LEMARI', inputQty)
            checkBol = True
        elif pilihMenu == 5:
            checkBol = True
            exec(open('transaction.py').read())
        else:
            print('Masukkan pilihan yang benar!')
            checkBol = False
    except ValueError:
        print('Inputan harus berupa angka!')
        continue


