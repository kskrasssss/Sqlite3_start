import sqlite3


# try:
#     sql_connect = sqlite3.connect('my_first_2_DataBase.db')
#     cursor = sql_connect.cursor()
#     print('DB create and connected)))))))))))))))')

#     sql_select_query = 'select sqlite_version()'
#     cursor.execute(sql_select_query)
#     record = cursor.fetchall() # отримання усіх рядки
#     print('version of DB: ', record)
#     cursor.close()

# try:
#     sql_connect = sqlite3.connect('my_first_2_DataBase.db')
#     create_table = '''
#         CREATE TABLE first_table(
#         id INTENGER PRIMARY KEY,
#         name TEXT NOT NULL,
#         email TEXT NOT NULL UNIQUE,
#         joining_date datetime,
#         salary REAL NOT NULL)'''


#     cursor = sql_connect.cursor()
#     print('DB connected)))))))))))))))')

#     cursor.execute(create_table)
#     sql_connect.commit()
#     print('table created')

#     cursor.close()


# try:
#     sql_connect = sqlite3.connect('my_first_2_DataBase.db')
#     cursor = sql_connect.cursor()
#     print('DB connected)))))))))))))))')

#     sql_insert = '''
#     INSERT INTO first_table(name, email, joining_date, salary)
#     VALUES('John', 'dfskfefj@gmail.com', '2024-12-09', 40000);
#     '''
#     count = cursor.execute(sql_insert)
#     sql_connect.commit()
#     print('Inserted', cursor.rowcount)
#     cursor.close()

def insert_vars_into_table(man_id, man_name, man_email, man_date, man_salary):
    try:
        sql_connect = sqlite3.connect('my_first_2_DataBase.db')
        cursor = sql_connect.cursor()
        print('DB connected)))))))))))))))')

        sql_insert_vars = '''
        INSERT INTO first_table
        (id, name, email, joining_date, salary)
        VALUES(?, ?, ?, ?, ?);
        '''

        data_tuple =(man_id, man_name, man_email, man_date, man_salary)
        cursor.execute(sql_insert_vars, data_tuple)
        sql_connect.commit()
        print('ok')
        cursor.close()

    except sqlite3.Error as error:
        print('Error with connection', error)

    finally:
        if sql_connect:
            sql_connect.close()
            print('Connection closed')

insert_vars_into_table(2, 'Carl', 'daewaei@gmail.com', '2023-04-07','20000.45' )
# Типи даних в базі даних. [NULL-нічого INTEGER-цілі числа REAL-дріб TEXT-рядки BLOB-бінарні(зображення)]
