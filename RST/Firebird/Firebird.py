import fdb

print('Введите путь до базы(Используйте localhost при подключении к локальной базе)')
path = input()
print('Введите логин')
username = input()
print('Введите пароль')
password = input()
con = fdb.connect(dsn=repr(str(path)), user=repr(str(username)), password=repr(str(password)))

cur = con.cursor() #Cursos объект

tables = cur.execute("show tables;")
print(tables) #Вывод таблиц из базы
SELECT = cur.execute("select * from test;")
#Вывод информации из таблицы тест
print(SELECT)
