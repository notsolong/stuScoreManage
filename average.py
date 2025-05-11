import sqlite3
import itertools
def average():
    try:
        print("所有学生成绩如下：")
        conn = sqlite3.connect('D:\PycharmProjects\pythonProject1\studentinfo.sqlite')
        cur = conn.cursor()
        sql = "select math from stuinfo "
        res = cur.execute(sql, )
        a = []  #创建列表，存放数学元组里的数据
        b = []
        c = []
        for values in res:
            x = list(values)
            a.append(x)
        x = list(itertools.chain.from_iterable(a))
        mave = sum(x) / len(x)
        print("学生的数学平均成绩：%.2f" % (mave))
        sql1 = "select english from stuinfo "
        ses = cur.execute(sql1, )
        for values in ses:
            y = list(values)
            b.append(y)
        y = list(itertools.chain.from_iterable(b))
        eave = sum(y) / len(y)
        print("学生的英语的平均成绩：%.1f" % (eave))
        sql1 = "select chinese from stuinfo "
        tes = cur.execute(sql1, )
        for values in tes:
            z = list(values)
            c.append(z)
        z = list(itertools.chain.from_iterable(b))
        cave = sum(z) / len(z)
        print("学生的语文的平均成绩：%.2f" % (cave))
        conn.commit()
        cur.close()  # 关闭游标对象
        conn.close()  # 关闭数据库连接
    except:
        print("学生成绩统计失败！")