# 获取老师基本信息，姓名、校区、工号
from typing import List

from tootchina.sqltool import get_sql_done


def getcardname() -> List:
    sql1 = """SELECT
        0,
        card.card_name,
        card.id
        FROM
        card
        """
    cur = get_sql_done(sql1)
    lim = []
    for i in cur:
        lim.append(list(i))
    return lim


def getteacherbasicinfo(request):
    serial = request.Get.get("serial")
    sql = f"""
    SELECT
    employee.`name`,
    employee.serial,
    campus.campus_name
    FROM
    employee ,
    campus
    WHERE
    employee.campus_id = campus.campus_id AND
    employee.serial = '{serial}'
    """
    cur = get_sql_done(sql)
    for item in cur:
        li = item
    print(li)


def getteachersallcourse():
    pass


# 获取老师卡牌明细，返回一个三维列表
def getteachercard(quest):
    serial = quest.GET.get("serial")
    sql = f"""
    SELECT
    Count(student_card.card_num) AA,
    card.card_name,
    card_id
    FROM
    student_card ,
    card
    WHERE
    student_card.employee_id = (SELECT employee.employee_id FROM employee WHERE employee.serial = '{serial}') AND
    student_card.card_id = card.id
    GROUP BY
    student_card.card_id
    ORDER BY card_id DESC
    """
    cur = get_sql_done(sql)
    # 用于生成固定格式且固定长度的列表,目前缺少一个卡牌名称参数问题。
    lii = getcardname()
    for item in cur:
        lii[item[2] - 1] = list(item)
    return lii


def getteacherclazz(quest)->List:
    serial = quest.GET.get("serail")
    sql = f"""
    SELECT DISTINCT
    stu_class_current.class_id,
    stu_class.`name`,
    SUBSTR(stu_class.`name` FROM 4 FOR 7) num
    FROM
    stu_class_current ,
    student ,
    stu_class
    WHERE
    student.student_id = stu_class_current.student_id AND
    student.campus_id = LCASE((SELECT
    employee.campus_id
    FROM
    employee
    WHERE
    employee.serial = '{serial}')) AND
    stu_class_current.class_id = stu_class.class_id
    ORDER BY num"""
    cur = get_sql_done(sql)
    # alist = []
    tlist = []
    for i in cur:
        # alist.append(list(i)[1])
        tlist.append(list(i)[:2])

    return tlist



def getteachercourse(quest)->List:
    serail = quest.GET.get("serial")
    sql = """
    
    
    """


    pass
