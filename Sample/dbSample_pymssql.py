# coding=utf8

"""
Description:Python连接sqlserver数据库，解决中文乱码问题

"""

import pymssql

# os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'

conn = pymssql.connect(host='Beta', user='Pdocw', password='123456', database='Curriculum_design', charset="GBK")
cur = conn.cursor()
# cur.execute('CREATE TABLE persons(id INT, name VARCHAR(100))')
# cur.executemany("INSERT INTO persons VALUES(%d, xinos.king)", [ (1, 'John Doe'), (2, 'Jane Doe') ])
# conn.commit()
cur.execute('SELECT * FROM kc')
row = cur.fetchone()
while row:
    # print("Cno=xinos.king, Cname=xinos.king ,Credit=%s" % (row[0], row[1],row[2]))
    # print("Cno=%s, Cname=%s ,Credit=%s" % (row[0], row[1], row[2]))
    print(row[0], row[1], row[2])
    row = cur.fetchone()
# cur.execute("SELECT * FROM persons WHERE salesrep LIKE 'J%'")
conn.close()
