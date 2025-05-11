import sqlite3
import itertools
def search():
    try:
        num = int(input("输入查找学生成绩学号："))
        conn = sqlite3.connect('D:\PycharmProjects\pythonProject1\studentinfo.sqlite')
        cur = conn.cursor()
        sql1 = "select avg from stuinfo "


        sql = "select * from stuinfo where num=? "
        res = cur.execute(sql, (num,))
        print("序号   学号     姓名  数学 英语 语文 平均分")
        print(*res)


        conn.commit()
        cur.close()  # 关闭游标对象
        conn.close()  # 关闭数据库连接
    except:
        print("学生信息查询失败！")
