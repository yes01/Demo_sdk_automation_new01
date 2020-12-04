# -*- coding: UTF-8 -*-
import traceback
import pymysql
from sshtunnel import SSHTunnelForwarder
from Common.basepage import logger


def xmain01(self,database,table,num):
    with SSHTunnelForwarder(
            ssh_address_or_host=("35.201.214.241", 22),  # ssh跳转机的地址
            ssh_username="user100",  # ssh的用户名
            ssh_pkey="C:/nginx-user100-ssh-key",  # ssh私钥地址
            ssh_private_key_password="",  # ssh私钥密码
            local_bind_address=("127.0.0.1", 10023),
            remote_bind_address=("10.140.0.94", 31007)) as server:  # 数据库地址
        server.start()
        myConfig = pymysql.connect(
            user="root",  # 数据库登录名
            passwd="CrazyCube!@#",  # 数据库密码
            host="127.0.0.1",  # 写死
            db=database,  # 数据库名称
            port=server.local_bind_port,
            cursorclass=pymysql.cursors.DictCursor)  # sql查询结果返回类型：DictCursor 为字典类型， 没有指定为 数组
        cursor = myConfig.cursor()
        try:
            sql = "select Value from {0} where StorageData ='{1}'  ORDER BY CreatedAtUtc DESC LIMIT 1 ".format(table,num)
            cursor.execute(sql)
            customers = cursor.fetchall()
            for customer in customers:
                logger.info("连接{0}库中{1}表成功，获取{2}验证码：{3}".format(database, table, num, customer["Value"]))

        except Exception as e:  # 捕捉异常，并打印
            traceback.print_exc()
            # 关闭数据库连接
        cursor.close()
        myConfig.close()

        return customer["Value"]


def xmain02(sql,sql01="select * from Level"):
    with SSHTunnelForwarder(
            ssh_address_or_host=("35.201.214.241", 22),  # ssh跳转机的地址
            ssh_username="user100",  # ssh的用户名
            ssh_pkey="C:/nginx-user100-ssh-key",  # ssh私钥地址
            ssh_private_key_password="",  # ssh私钥密码
            local_bind_address=("127.0.0.1", 10023),
            remote_bind_address=("10.140.0.94", 31007)) as server:  # 数据库地址
        server.start()
        myConfig = pymysql.connect(
            user="root",  # 数据库登录名
            passwd="CrazyCube!@#",  # 数据库密码
            host="127.0.0.1",  # 写死
            db="CubeAgePlatform",  # 数据库名称
            port=server.local_bind_port,
            cursorclass=pymysql.cursors.DictCursor)  # sql查询结果返回类型：DictCursor 为字典类型， 没有指定为 数组
        cursor = myConfig.cursor()
        cursor.execute(sql)
        cursor.execute(sql01)
        myConfig.commit()  # 统一提交

        # 关闭数据库连接
        cursor.close()
        myConfig.close()

def er():
    # 连接数据库
    connect = pymysql.Connect(
        host='8.210.102.39',
        port=31007,
        user='root',
        passwd='CrazyCube!@#',
        db='CubeAgePlatform',  # 数据库名称
        charset='utf8',
        cursorclass=pymysql.cursors.DictCursor) # sql查询结果返回类型：DictCursor 为字典类型， 没有指定为 数组
    cursor = connect.cursor()
    try:
        sql = "select Value from {0} where StorageData ='{1}'  ORDER BY CreatedAtUtc DESC LIMIT 1 ".format("AuthenticationCode","010132@gmail.com")
        cursor.execute(sql)
        customers = cursor.fetchall()
        for customer in customers:
            logger.info("连接库成功")

    except Exception as e:  # 捕捉异常，并打印
        traceback.print_exc()
            # 关闭数据库连接
    cursor.close()
    connect.close()

    return customer["Value"]

