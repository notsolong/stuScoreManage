import sqlite3
def printall():
    try:
        print("所有学生成绩如下：")
        print("序号    学号    姓名  数学 英语 语文 平均分")
        conn = sqlite3.connect('D:\PycharmProjects\pythonProject1\studentinfo.sqlite')
        cur = conn.cursor()
        sql = "select * from stuinfo where num like num "
        res = cur.execute(sql)

        for item in res:
            print(item)
        conn.commit()
        cur.close()  # 关闭游标对象
        conn.close()  # 关闭数据库连接
    except:
        print("查询全部学生信息失败！")