from flask import Blueprint,render_template,redirect,request
from function.delete import delete
import pymysql
import datetime



conn = pymysql.connect(host="localhost" , user='root' , password='' , database='cms')

update2 = Blueprint('update_courses',__name__)
    



def courses_add(request):
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
    
def update_courses(id):
        
        name = request.form.get("name")
        duration = request.form.get("duration")
        fees = request.form.get("fees")

        with conn.cursor() as cur:
            sql = "UPDATE courses SET name=%s, duration=%s, fees=%s WHERE course_id=%s"
            values = ( name, duration, fees, id)
            cur.execute(sql, values)
            conn.commit()

            return 2
        



@update2.route("/coursesupdate/<id>" ,methods=['GET','POST'])
def updatecourses(id):
    if request.method == 'GET':
        with conn.cursor() as cur:
            sql = "SELECT * FROM courses WHERE course_id=%s"
            values = (id)
            cur.execute(sql, values)
            data = cur.fetchone()
        return render_template("coursesupdate.html", datas=data)
    if request.method == 'POST':
        status = update_courses(id)
        if status == 2:
            return redirect("/coursestable")
        else:
            return "INVALID"


@update2.route("/coursestable/<param>/<id>")
def  coursesdelete(param,id):
   if param=="delete":
        delete("courses", "course_id ", id)
        return redirect("/coursestable")