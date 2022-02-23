import buy

checkBol = False

print('========================= RUMAH TANGGA =========================')
print('Silahkan pilih Barang')
print('1. Televisi')
print('2. Kulkas')
print('3. Rice Cooker')
print('4. Setrika')
print('5. Kembali')

while checkBol == False:
    try:
        pilihMenu = int(input('Silahkan Masukkan Pilihan: '))

        if pilihMenu == 1:
            inputQty = int(input('Silahkan Masukkan Jumlah Barang: '))
            buy.buyFunction('TELEVISI', inputQty)
            checkBol = True
        elif pilihMenu == 2:
            inputQty = int(input('Silahkan Masukkan Jumlah Barang: '))
            buy.buyFunction('KULKAS', inputQty)
            checkBol = True
        elif pilihMenu == 3:
            inputQty = int(input('Silahkan Masukkan Jumlah Barang: '))
            buy.buyFunction('RICE COOKER', inputQty)
            checkBol = True
        elif pilihMenu == 4:
            inputQty = int(input('Silahkan Masukkan Jumlah Barang: '))
            buy.buyFunction('SETRIKA', inputQty)
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


