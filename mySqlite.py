import sqlite3

conn = sqlite3.connect('test.db')
print ("打开数据库成功")
# 创建表
# c = conn.cursor()
# c.execute('''CREATE TABLE PROGRAM_CONFIG
#        (ID INT PRIMARY KEY     NOT NULL,
#        PROGRAM_NAME           TEXT    NOT NULL,
#        PROGRAM_PATH           TEXT    NOT NULL
#        );''')
# print ("表创建成功");
# conn.commit()
# conn.close()


# 插入表
#
# c = conn.cursor()
#
# c.execute("INSERT INTO PROGRAM_CONFIG (ID,PROGRAM_NAME,PROGRAM_PATH) \
#       VALUES (1, '微信', 'D:/WeChat/WeChat.exe' )");
#
# c.execute("INSERT INTO PROGRAM_CONFIG (ID,PROGRAM_NAME,PROGRAM_PATH) \
#       VALUES (2, 'VS2010','')");
#
# c.execute("INSERT INTO PROGRAM_CONFIG (ID,PROGRAM_NAME,PROGRAM_PATH) \
#       VALUES (3, 'VSCODE','D:/VS Code/Microsoft VS Code/Code.exe' )");
#
# c.execute("INSERT INTO PROGRAM_CONFIG (ID,PROGRAM_NAME,PROGRAM_PATH) \
#       VALUES (4, '钉钉', '' )");
#
# c.execute("INSERT INTO PROGRAM_CONFIG (ID,PROGRAM_NAME,PROGRAM_PATH) \
#       VALUES (5, 'ORACLE', '' )");
#
# c.execute("INSERT INTO PROGRAM_CONFIG (ID,PROGRAM_NAME,PROGRAM_PATH) \
#       VALUES (6, 'OFFICE', '' )");
#
# c.execute("INSERT INTO PROGRAM_CONFIG (ID,PROGRAM_NAME,PROGRAM_PATH) \
#       VALUES (7, 'EXCEL', '' )");
#
# conn.commit()
# print ("数据插入成功");
# conn.close()


# # 查询表
# c = conn.cursor()
# cursor = c.execute("SELECT ID, PROGRAM_NAME,PROGRAM_PATH  from PROGRAM_CONFIG")
# # for row in cursor:
# #    print ("ID = ", row[0])
# #    print ("PROGRAM_NAME = ", row[1])
# #    print ("PROGRAM_PATH = ", row[2],"\n")
#
# print ("查询成功");
# conn.close()

# 更新表
# c = conn.cursor()
# c.execute("UPDATE PROGRAM_CONFIG set PROGRAM_NAME = '',PROGRAM_PATH='' where ID=1")
# conn.commit()
# cursor = c.execute("SELECT ID, PROGRAM_NAME,PROGRAM_PATH  from PROGRAM_CONFIG")
# for row in cursor:
#    print ("ID = ", row[0])
#    print ("PROGRAM_NAME = ", row[1])
#    print ("PROGRAM_PATH = ", row[2],"\n")
# conn.close()

# 查询结果保存在字典类型中
def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d
con = sqlite3.connect('test.db') #打开在内存里的数据库
con.row_factory = dict_factory
cur = con.cursor()
print (123)
cur.execute("SELECT ID, PROGRAM_NAME,PROGRAM_PATH  from PROGRAM_CONFIG")
conn.close()
dics=cur.fetchall()
for dic in dics:
    if u'微信'==dic['PROGRAM_NAME']:
        print (1)



# print (cur.fetchone()["PROGRAM_PATH"])