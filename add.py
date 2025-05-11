import sqlite3
def add():
    try:
        conn = sqlite3.connect('D:\PycharmProjects\pythonProject1\studentinfo.sqlite')
        cur = conn.cursor()
        a = []
        num = int(input("输入学生学号："))

        name = input("请输入学生姓名：")

        math = int(input("输入学生英语成绩："))
        a.append(math)
        chinese = int(input("输入学生数学成绩："))
        a.append(chinese)
        english =int(input("输入学生语文成绩："))
        a.append(english)
        avg=sum(a)/len(a)
        sql = "insert into stuinfo(num,name,math,chinese,english ,avg) values (?, ?, ?, ?,?,?)"
        cur.execute(sql, (num, name, math, chinese, english,round(avg,1)))
        print("学生成绩录入成功")
        conn.commit()
        cur.close()  # 关闭游标对象
        conn.close()  # 关闭数据库连接
    except:
        print("学生信息录入失败！")

