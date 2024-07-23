from flask import redirect,render_template,request
import pymysql
import datetime



conn = pymysql.connect(host="localhost" , user='root' , password='' , database='cms')

def guardian_add(req):
    student_id=req.form.get("student_id")
    father_name=req.form.get("father_name")
    mother_name=req.form.get("mother_name")
    address=req.form.get("address")
    mobile=req.form.get("mobile")
    email=req.form.get("email")
    flag = 0

    with conn.cursor() as cur:
        sql="select * from students where student_id=%s"
        data=(student_id)
        status= cur.execute(sql,data)
        if status:
            flag=1

    if flag==1:
        with conn.cursor() as cur:  
            sql="""INSERT INTO guardians(student_id,father_name,mother_name,address,mobile,email)Values(%s,%s,%s,%s,%s,%s)"""
            values=(student_id,father_name,mother_name,address,mobile,email,)
            cur.execute(sql,values)
            conn.commit()
        return 1
    else:
        return 0