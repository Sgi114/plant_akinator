import MySQLdb

def setup():
    cnx = MySQLdb.connect(
        host='localhost',
        user='root',
        password='password',
        db='dbname'
    )
    cursor = cnx.cursor()
    return cnx,cursor
