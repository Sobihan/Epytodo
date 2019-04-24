from app import models

def set_connection():
    try:
        data_base, connect = connection()
        result = ""
        cursor = connect.cursor()
        cursor . execute ("SELECT * from user")
        result = cursor.fetchall()
        cursor.close()
        connect.close()
    except Exception as e :
        print("Database request error: ", e)
    close_data(connect, data_base)
    return (result)