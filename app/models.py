import pymysql as sql
from app import app

def connection() :
    try:
        connect = sql.connect(host = "127.0.0.1",
        unix_socket = "None",
        user ="bshiron",
        passwd ="secretpass",
        db ='epytodo'
        )
        data = connect
        sql = "\.epytodo.sql"
        return (connect, data)
    except Exception as e :
        print ("Caught an exception : ", e)
        return (None, None)


def close_data(connect, data):
    try:
        data.close()
        connect.close()
    except Exception as e:
        print("Caught an exception : ", e)