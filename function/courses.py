from flask import redirect,render_template,request
import pymysql
import datetime



conn = pymysql.connect(host="localhost" , user='root' , password='' , database='cms')

def courses_add():
    courseId=request.form.get("course_id")
    name=request.form.get("name")
    duration=request.form.get("duration")
    fees=request.form.get("fees")

    with conn.cursor() as cur:
        sql="INSERT into courses (course_id, name, duration, fees) values(%s, %s, %s, %s)"
        values = (courseId, name, duration, fees)
        cur.execute(sql,values)
        conn.commit()

        return 1