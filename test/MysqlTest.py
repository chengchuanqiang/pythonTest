import pymysql


# 获取数据库连接
def getConn(host, userName, pwd, dbName, port):
    return pymysql.connect(host=host, user=userName, password=pwd, database=dbName, port=port)


host = "127.0.0.1"
port = 3306
userName = "root"
pwd = "123456"
dbName = "test"
db = getConn(host, userName, pwd, dbName, port)
# 使用cursor() 方法获取操作游标
cursor = db.cursor()

# SQL处理语句
insertSql = "insert into user(username,age) values('%s','%d')" % ("ccq", 33)
querySql = "select * from user where id = '%d'" % 2
updateSql = "update user set age = age + 1 where id = '%d'" % 2
deleteSql = "delete from user where id = '%d'" % 1
try:
    num = cursor.execute(insertSql)
    db.commit()
    print("插入执行成功条数:", num)

    cursor.execute(querySql)
    res = cursor.fetchall()
    print("res : ", res)
    print("查询出数据条数:", res.__len__())
    for row in res:
        id = row[0]
        name = row[1]
        age = row[2]
        create_time = row[3]
        update_time = row[4]
        print("id=%s,name=%s,age=%s,create_time=%s,update_time=%s" % (id, name, age, create_time, update_time))

    num = cursor.execute(updateSql)
    db.commit()
    print("更新执行成功条数:", num)

    num = cursor.execute(deleteSql)
    db.commit()
    print("删除执行成功条数:", num)

except Exception as e:
    print("发生异常，异常信息:", e)
    # 发生错误时进行回滚
    db.rollback()
finally:
    if db:
        # 关闭数据库连接
        db.close()
