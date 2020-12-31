# １.导入pyodbc组件
import pyodbc

# ２.调用pyodbc类中的connect()方法创建连接对象。
conn = pyodbc.connect(r'DRIVER={SQL Server Native Client 11.0};'
                      r'SERVER=Beta;'
                      r'DATABASE=Curriculum_design;'
                      r'UID=Pdocw;'
                      r'PWD=123456'
                      )
# 3.通过该连接对象中的cursor()方法创建cursor（游标）对象。
cursor = conn.cursor()
# 4.对数据库的增删改查都是通过cursor对象中相关方法来执行的。
cursor.execute("select * from kc")
# 5.操作完数据库后，可以通过fetchall()方法获取到相应的数据。
rows = cursor.fetchall()
for row in rows:
    # print(row.Cno,row.Cname,row.Credit)
    print('{x:^{y}s}\t'.format(x=row.Cno,
                               y=15 - len(row.Cno.encode('GBK')) + len(row.Cno)), end='')
    print('{x:^{y}s}\t'.format(x=row.Cname,
                               y=15 - len(row.Cname.encode('GBK')) + len(row.Cname)), end='')
    print('{x:^{y}}\t'.format(x=row.Credict,
                              y=15 - 2), end='')
    print()

conn.close()
