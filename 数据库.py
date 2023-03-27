import sqlite3   # 数据库DB文件

firstdb = sqlite3.connect(r'数据\first.db')


def cx():  # 查询数据
    query_sql = "select * from info"
    for result in firstdb.execute(query_sql):
        print(result)


def sc():  # 删除数据
    delete_sql = 'delete from info where id = 1'
    firstdb.execute(delete_sql)
    firstdb.commit()


def cr():  #  插入
    insert_sql= "insert into info(title,content,author)values ('第{}个标题', '随机的第{}个内容', '匿名')"
    for  i in range(10,20):
        sql = insert_sql.format(i,i*2)
        firstdb.execute(sql)
        firstdb.commit()


def gx():  # 更新
    update_sql = "update info set author = '不匿名' where id >= 4"
    firstdb.execute(update_sql)


if __name__ == '__main__':
    cx()
