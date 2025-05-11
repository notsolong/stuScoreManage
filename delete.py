import sqlite3
def delete():
    conn = sqlite3.connect('D:\PycharmProjects\pythonProject1\studentinfo.sqlite')
    cur = conn.cursor()
    try:
       num = int(input("输入要删除学生成绩的学号："))

       sql = "delete from stuinfo where num=?"
       cur.execute(sql, (num,))
       print("学生成绩删除成功")
       conn.commit()
       cur.close()  # 关闭游标对象
       conn.close()  # 关闭数据库连接
    except :
        print("学生信息删除失败！")











