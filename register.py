import datetime as dt
import connection as con

class registerClass():
    forbidenSign = '@ ! # $ % ^ & * ( ) - + < > ? / \ | ~'
    defaultSign = False

    def forbidenCharacter(self, a, type):
        if type in ['user','pasw','name','rePasw','address', 'city', 'zipCode']:
            for rec in a:
                if rec in self.forbidenSign.split():
                    print(f"Jangan gunakan karakter {self.forbidenSign}")
                    self.defaultSign = False
                else:
                    self.defaultSign = True
        elif type == 'email':
            for rec in a:
                if rec in self.forbidenSign.split()[1:]:
                    print(f"Jangan gunakan karakter {self.forbidenSign.split()[1:]}")
                    self.defaultSign = False
                else:
                    self.defaultSign = True

    def emailVerification(self, email):
        userContain = '1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ._'
        karakterKhusus = '~!#$%^&*()+<>?/|}{]['
        result = ''

        try:
            cekAt = email.count('@')
            getAwalan = email[0]
            getUser = email[0:email.index('@')]
            getHostingExt = email[email.index('@') + 1:]
            getHosting = getHostingExt[:getHostingExt.index('.')]
            getExtFull = getHostingExt[getHostingExt.index('.') + 1:]
            getExt1 = ''
            getExt2 = ''
            flag = True
            flag2 = True

            if '.' in getExtFull:
                getExt1 = getExtFull[:getExtFull.index('.')]
                getExt2 = getExtFull[getExtFull.index('.') + 1:]

            for rec in getUser:
                if rec not in userContain:
                    flag = False
                    break

            for rec in email:
                if rec in karakterKhusus:
                    flag2 = False
                    break

            if flag == True and getAwalan.isalnum() and (getHosting.isalpha() or getHosting.isnumeric() == False) and (
                    (getExt1 == '' and getExtFull.isalpha() and len(getExtFull) <= 5) or (
                    getExt1 != '' and getExt2 != '' and getExt1.isalpha() and getExt2.isalpha() and len(
                    getExt1) <= 5 and len(getExt1) <= 5)) and flag2 == True and cekAt == 1:
                self.defaultSign = True
            else:
                result += 'Email Invalid! \n'
                if flag == False:
                    result += 'Format username yang anda masukkan salah \n'

                if getAwalan.isalnum() == False:
                    result += 'Format username yang anda masukkan salah \n'

                if getHosting.isnumeric() == True:
                    result += 'Format hosting yg anda masukkan salah \n'

                if (getExt1 == '' and (
                        getExtFull.isalpha() == False or len(getExtFull) <= 0 or len(getExtFull) > 5)) or (
                        getExt1 != '' and getExt2 != '' and (
                        getExt1.isalpha() == False or getExt2.isalpha() == False or len(getExt1) <= 0 and len(
                        getExt1) > 5)):
                    result += 'Format extensi yg anda masukkan salah \n'

                if flag2 == False:
                    result += 'Format email salah, terdapat simbol/karakter khusus \n'

                if cekAt == 0:
                    result += 'Format email salah, tidak terdapat @ \n'

                if cekAt > 1:
                    result += 'Format email salah, terlalu banyak tanda @ \n'

                self.defaultSign = False
        except ValueError:
            result += 'Format Email Salah \n'
            self.defaultSign = False

        return result

register = registerClass()

print('========================= MENU REGISTRASI =========================')

register = registerClass()

while register.defaultSign == False:
    user = input('Please Input Username: ')
    con.cur.execute(f"SELECT * FROM USER_LOGIN WHERE USERNAME = '{user}'")
    register.forbidenCharacter(user,'user')
    try:
        checkUser = con.cur.fetchone()[0]
        print('Username telah terdaftar!')
        register.defaultSign = False
    except:
        checkUser = None
        register.defaultSign = True

register.defaultSign = False

while register.defaultSign == False:
    pasw = input('Please Input Password: ')
    register.forbidenCharacter(pasw, 'pasw')

register.defaultSign = False

while register.defaultSign == False:
    rePasw = input('Please Re-Type Password: ')
    register.forbidenCharacter(rePasw, 'rePasw')
    if rePasw != pasw:
        print('Password tidak sesuai')
        register.defaultSign = False
    else:
        register.defaultSign = True

register.defaultSign = False

while register.defaultSign == False:
    name = input('Please Input Full Name: ')
    register.forbidenCharacter(name, 'name')

register.defaultSign = False

while register.defaultSign == False:
    email = input('Please Input Email: ')
    register.forbidenCharacter(email, 'email')
    print(register.emailVerification(email))

register.defaultSign = False

while register.defaultSign == False:
    phone = input('Please Input Phone Number: ')
    try:
        convertPhone = int(phone)
        register.defaultSign = True
    except:
        print('Input no telpon harus berupa angka')

register.defaultSign = False

while register.defaultSign == False:
    address = input('Please Input Address: ')
    register.forbidenCharacter(address, 'address')

register.defaultSign = False

while register.defaultSign == False:
    city = input('Please Input City: ')
    register.forbidenCharacter(city, 'city')
    if not city.isalpha():
        print('Kota harus alphabetic')
        register.defaultSign = False

register.defaultSign = False

while register.defaultSign == False:
    zipCode = input('Please Input Zip Code: ')
    try:
        convertZipCode = int(zipCode)
        register.defaultSign = True
    except:
        print('Input zip code harus berupa angka')

getTime = dt.date.today()

con.cur.execute('SELECT MAX(USERID) FROM USER_LOGIN')
try:
    getMaxUserId = con.cur.fetchone()[0]
except:
    getMaxUserId = None

if getMaxUserId is None:
    userId = str(getTime.year) + str(getTime.month).zfill(2) + '1'.zfill(4)
else:
    concatId = str(int(getMaxUserId) + 1)
    userId = concatId.zfill(4)

try:
    con.cur.execute(f"INSERT INTO USER_LOGIN VALUES ('{userId}','{user}','{pasw}','{getTime}');")
    con.cur.execute(f"INSERT INTO CUSTOMERS VALUES ('{userId}','{name}','{email}','{phone}','{address}','{city}','{zipCode}');")
    con.conn.commit()
    print('Data berhasil disimpan!')
    exec(open('main.py').read())
except:
    con.conn.rollback()





