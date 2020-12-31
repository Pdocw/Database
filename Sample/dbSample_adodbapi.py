import adodbapi

adodbapi.adodbapi.verbose = False  # adds details to the sample printout

Cfg = {'server': 'Beta', 'password': '123456', 'db': 'Curriculum_design'}
constr = r"Provider=SQLOLEDB.1; Initial Catalog=%s; Data Source=%s; user ID=%s; Password=%s; " % (
Cfg['db'], Cfg['server'], 'Pdocw', Cfg['password'])
conn = adodbapi.connect(constr)
cur = conn.cursor()
# sql='''select * from softextBook where title='{0}' and remark3!='{1}''''.format(bookName,flag)
sql = 'select * from xsxx'
cur.execute(sql)
row = cur.fetchone()
while row:
    # print("Cno=xinos.king, Cname=xinos.king ,Credit=%s" % (row[0], row[1],row[2]))
    print("Cno=%s, Cname=%s ,Credit=%s" % (row[0], row[1], row[2]))
    row = cur.fetchone()
# cur.close()
# 假设proName有三个参数,最后一个参数传了null
# ret=cur.callproc('procName',(parm1,parm2,None))
cur.close()
