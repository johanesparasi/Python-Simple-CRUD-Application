import connection as conn
import datetime as dt
import globalVariable as gv

def buyFunction(jenisBarang, qty):
    conn.cur.execute(f"SELECT STOCK FROM STOCK WHERE DESCRIPTION = '{jenisBarang}'")
    getStock = conn.cur.fetchone()[0]
    conn.cur.execute(f"SELECT ID_BARANG FROM STOCK WHERE DESCRIPTION = '{jenisBarang}'")
    getIdBarang = conn.cur.fetchone()[0]
    sisaStock = getStock - qty
    getTime = dt.datetime.today()
    conn.cur.execute(f"SELECT USERID FROM USER_LOGIN WHERE USERNAME = '{gv.username}'")
    getUserID = conn.cur.fetchone()[0]
    conn.cur.execute(f"SELECT MAX(ID_TRANSACTION) FROM TRANSACTION")

    try:
        getTransactionID = conn.cur.fetchone()[0]
    except:
        getTransactionID = None

    if getTransactionID is None:
        getTransactionID = str(getTime.year) + str(getTime.month).zfill(2) + str(getTime.day) + '1'.zfill(7)
    else:
        concat = str(int(getTransactionID) + 1)
        getTransactionID = concat.zfill(7)

    try:
        conn.cur.execute(f"UPDATE STOCK SET STOCK = '{sisaStock}' WHERE DESCRIPTION = '{jenisBarang}'")
        conn.cur.execute(f"INSERT INTO TRANSACTION VALUES ('{getTransactionID}','{getIdBarang}','{getUserID}','{qty}','{getTime}')")
        conn.conn.commit()
        print('Berhasil Belanja')
    except:
        conn.conn.rollback()
        print('Terdapat Kesalahan Sistem, silahkan ulangi kembali')

    exec(open('transaction.py').read())

        