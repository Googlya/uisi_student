import fdb
import getpass

print('Введите путь до базы(Используйте localhost при подключении к локальной базе)')
path = input()
print('Введите логин')
username = input()
print('Введите пароль')
password = getpass.getpass()
con = fdb.connect(dsn=path, user=username, password=password)

cur = con.cursor()

cur.execute("SELECT * FROM RDB$RELATIONS")
print(cur.fetchall())

print('______________________')

cur.execute("SELECT * FROM test")
print(cur.fetchmany(5))
