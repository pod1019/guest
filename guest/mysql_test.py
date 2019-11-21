import pymysql.cursors
# Connect to the database
connection = pymysql.connect(host='127.0.0.1',user='root',password='fjj123',
                             db='guest',charset='utf8',cursorclass=pymysql.cursors.DictCursor)
try:
    with connection.cursor() as cursor:
        # Create a new record
        sql = 'insert into sign_guest (realname, phone, email, sign, event_id, create_time) values ("小明",13388889999,"xm@mail.com",0,1,NOW());'
        cursor.execute(sql)

    # connection is not autocommit by default. So you must commit to save上面的虽然insert了，但是不会自动提交的，所以要执行下面的connection.commit(),数据库里才有数据
    # your changes.
    connection.commit()

    with connection.cursor() as cursor:
    # Read a single record
        sql = 'select realname,phone,email,sign from sign_guest where phone=%s'
        cursor.execute(sql,('13388889999'))
        result = cursor.fetchone()
        print(result)
finally:
    connection.close()

#django-bootstrap3-11.1.0
# django 2.2