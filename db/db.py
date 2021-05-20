import sqlite3
con = sqlite3.connect(':memory:')    # 프로젝트 실행시 info.db로 바꾸면 db 파일 생성
cursor = con.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS info (email VARCHAR(30) NOT NULL, id VARCHAR(20) 
                NOT NULL UNIQUE, password VARCHAR(20) NOT NULL, created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP);''')
cursor.execute("INSERT INTO info (email, id, password) VALUES('admin','admin','admin');")

def user_login(tup):
    try:
        find = ("SELECT * FROM 'info' WHERE id = ? AND password = ?")
        cursor.execute(find, tup)
        return (cursor.fetchone())
    except:
        return False


def user_signup(tup):
    try:
        cursor.execute(
            "INSERT INTO 'info' (email, id, password) VALUES (?, ?, ?)",
            tup
        )
        con.commit()
        return True
    except Exception as ex:
        print("ERROR: ", ex)
        return False

def check_ID(tup):
    try:
        find = ("SELECT id FROM 'info' WHERE email = ?")
        cursor.execute(find, (tup,))
        return cursor.fetchone()
    except Exception as e:
        print("ERROR db: ", e)
        return False

def check_PW(tup):
    try:
        find = ("SELECT password FROM 'info' WHERE email = ? AND id = ?")
        cursor.execute(find, tup)
        return cursor.fetchone()
    except Exception as e:
        print("ERROR db: ", e)
        return False


# def user_signIn()

# import mysql.connector
#
# con = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     passwd="",
#     database="testing"
# )
#
# cursor = con.cursor()
#
# def user_login(tup):
#     try:
#         cursor.execute("SELECT * FROM `info` WHERE `id`=%s AND `password`=%s", tup)
#         return cursor.fetchone()
#     except Exception as ex:
#         print("ERROR: ", ex)
#         return False

# def user_signup(tup):
#     try:
#         cursor.execute(
#             "INSERT INTO `info` (`email`, `id`, `password`, `created_at`) VALUES (%s, %s, %s, current_timestamp())",
#             tup
#         )
#         con.commit()
#         return True
#     except Exception as ex:
#         print("ERROR: ", ex)
#         return False