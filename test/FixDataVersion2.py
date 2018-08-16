# coding=utf-8

import pymysql
import datetime
import json
import uuid


# 获取连接
def getConn(host, port, user, passwd, db, charset):
    # myConn = pymysql.connect(host='10.80.87.166', port=3306, user='root', passwd='root', db='jarvis', charset='utf8')
    if charset is None:
        charset = "utf8"
    myConn = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db, charset=charset)
    return myConn


#  得到原始数据的id 列表,  以及以 原始的(id 为键， 元祖对象为val 构造map 结构) 对比更新的参照 map 结构
def getOriginData():
    # host = "10.80.87.166"
    # port = "3306"
    # user = "root"
    # passwd = "root"
    # db = "jarvis"
    # charset = "utf8"

    host = "127.0.0.1"
    port = 3306
    user = "root"
    passwd = "root"
    db = "Test"
    charset = "utf8"

    conn = getConn(host, port, user, passwd, db, charset)
    # 创建游标
    cursor = conn.cursor()
    # 查询 worksheet_dir 原始数据
    cursor.execute(
        "select table_id, conditions, work_sheet_data_update_time, engine_type, unique_mark from worksheet_dir WHERE flag_type = 2 and status = 1 ")
    results = cursor.fetchall()
    idDataMap = {}  # 以id 为键， 元祖对象为val 构造map 结构
    idList = []  # 存储id
    for row in results:
        if row[0] is None:
            print("Error=====>>Nullabletableid = %s" % \
                  (row[0],))
            continue
        idList.append(row[0])
        idDataMap[row[0]] = (row[0], row[1], row[2], row[3], row[4])
        print("tableid = %s, conditions = %s,worksheetDataUpdateTime = %s, engineType = %s" % \
              (row[0], row[1], row[2], row[3]))

    cursor.execute("select id, columns, sync_time, engine_type from data_set where id in %s", [idList])
    newdata = cursor.fetchall()
    engineTypeMap = {"druid": 1, "clickhouse": 2}
    newIdDataMap = {}
    for row in newdata:
        tempEngine = row[3]
        if row[3] is not None:
            tempEngine = engineTypeMap.get(row[3])
        newIdDataMap[row[0]] = (row[0], row[1], row[2], tempEngine)

    conn.commit()
    # 关闭游标
    cursor.close()
    # 关闭连接
    conn.close()

    return idList, idDataMap, newIdDataMap


def parseType(srcType):
    defaultStr = "string"
    typeDic = {}
    typeDic["tinyint"] = "double"
    typeDic["smallint"] = "double"
    typeDic["int"] = "double"
    typeDic["integer"] = "double"
    typeDic["bigint"] = "double"
    typeDic["float"] = "double"
    typeDic["double"] = "double"
    typeDic["double precision"] = "double"
    typeDic["decimal"] = "double"
    typeDic["numeric"] = "double"
    typeDic["real"] = "double"
    typeDic["timestamp"] = "datetime"
    typeDic["datetime"] = "datetime"
    typeDic["date"] = "date"

    if srcType is None or "" == srcType.strip():
        return defaultStr
    return typeDic.get(str(srcType).lower(), defaultStr)


# 解析 columns 到conditions
def parseConditions(conlumns):
    if conlumns is None or conlumns.strip() == "":
        return ""
    jsonObj = json.loads(conlumns)
    conditionList = []
    for obj in jsonObj:
        obj["type"] = parseType(obj["type"])
        obj["uuid"] = str(uuid.uuid1()).replace("-", "")
        conditionList.append(obj)
    return json.dumps(conditionList)


def runTask():
    # host = "10.80.87.166"
    # port = "3306"
    # user = "root"
    # passwd = "root"
    # db = "jarvis"
    # charset = "utf8"

    host = "127.0.0.1"
    port = 3306
    user = "root"
    passwd = "root"
    db = "Test"
    charset = "utf8"

    conn = getConn(host, port, user, passwd, db, charset)
    # 创建游标
    cursor = conn.cursor()
    idList, idDataMap, newIdDataMap = getOriginData()
    sqlItems = ["table_id", "conditions", "work_sheet_data_update_time", "engine_type", "unique_mark"]
    for dataKey, dataVal in idDataMap.items():
        updatesqlstr = "update worksheet_dir set work_sheet_status = 1 , work_sheet_update_status = 2"
        updatesqlitemVals = []  # 需要更新的字段 (现在为空)
        newDataVal = newIdDataMap.get(dataKey)
        needUpdate = False
        first = True
        # 构造 sql 语句
        updatesqlstr = updatesqlstr + " , conditions = %s"
        updatesqlitemVals.append(parseConditions(newDataVal[1]))

        updatesqlstr = updatesqlstr + ", work_sheet_data_update_time = %s "
        updatesqlitemVals.append(datetime.datetime.strftime(newDataVal[2], '%Y-%m-%d %H:%M:%S'))

        updatesqlstr = updatesqlstr + ", engine_type = %s "
        updatesqlitemVals.append(newDataVal[3])

        updatesqlstr = updatesqlstr + ", unique_mark = %s "
        updatesqlitemVals.append(newDataVal[0])

        updatesqlstr = updatesqlstr + " WHERE table_id = %s "
        updatesqlitemVals.append(dataKey)

        print("拼接更新sql 语句为==》 %s, 参数列表为=》 %s" % (updatesqlstr, updatesqlitemVals))
        try:
            cursor.execute(updatesqlstr, tuple(updatesqlitemVals))
        except Exception as msg:
            print("Error 更新出现异常 异常为=》%s 拼接更新sql 语句为==》 %s, 参数列表为=》 %s" % (msg, updatesqlstr, updatesqlitemVals))

    conn.commit()
    # 关闭游标
    cursor.close()
    # 关闭连接
    conn.close()


runTask()
