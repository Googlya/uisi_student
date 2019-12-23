import fdb
import getpass

print('Введите путь до базы(Используйте localhost при подключении к локальной базе)')
path = input()
kov_path = repr(str(path))
print('Введите логин')
username = input()
kov_user = repr(str(username))
print('Введите пароль')
password = getpass.getpass()
kov_pass = repr(str(password))
print(password)
con = fdb.connect(dsn= kov_path, user= kov_user, password=kov_pass)

cur = con.cursor() #Cursos объект

tables = cur.execute("show tables;")
print(tables) #Вывод таблиц из базы
SELECT = cur.execute("select * from test;")
#Вывод информации из таблицы тест
print(SELECT)
