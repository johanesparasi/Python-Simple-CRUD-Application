import connection as con
import globalVariable as gv

checkUserPasw = False

while checkUserPasw == False:
    print('Masukkan Username dan Password')
    user = input('Username : ')
    pasw = input('Password : ')

    con.cur.execute(f"SELECT * FROM USER_LOGIN WHERE USERNAME = '{user}'")
    try:
        checkUser = con.cur.fetchone()[0]
    except:
        checkUser = None

    if checkUser is None:
        print('Username belum terdaftar!')
        checkUserPasw = False
    else:
        con.cur.execute(f"SELECT * FROM USER_LOGIN WHERE PASSWORD = '{pasw}'AND USERNAME = '{user}'")
        try:
            checkPasw = con.cur.fetchone()[0]
        except:
            checkPasw = None

        if checkPasw is None:
            print('Password yang anda masukkan salah!')
            checkUserPasw = False
        else:
            print('Berhasil Login!')
            gv.username = user
            exec(open('transaction.py').read())
            checkUserPasw = True
